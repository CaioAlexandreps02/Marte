using System.IO;
using Marte.Player;
using Marte.World;
using UnityEditor;
using UnityEngine;
using UnityEngine.Rendering;

namespace Marte.EditorTools
{
    // Builds the gameplay scene: terrain streamer, water, first-person player and dust fog.
    public static class JezeroSceneSetup
    {
        [MenuItem("Marte/Scene/Setup World, Water and Player")]
        public static void Setup()
        {
            var meta = JezeroMetadata.Load();
            var info = AssetDatabase.LoadAssetAtPath<JezeroWorldInfo>(JezeroTerrainImporter.WorldInfoPath);
            if (info == null)
            {
                Debug.LogError("[Marte] JezeroWorldInfo not found. Run Marte/Terrain/Import Jezero first.");
                return;
            }

            Replace("Jezero");
            Replace("World");
            Replace("Landmarks");
            Replace("Water");
            Replace("Player");
            Replace("Main Camera");

            CreateWater(meta, info);
            var player = CreatePlayer(meta, info);
            CreateWorld(info, player.transform);
            CreateLandmarks(info);
            SetupFog();
            // Objects created from code don't dirty the scene by themselves; without this, saving skips it.
            UnityEditor.SceneManagement.EditorSceneManager.MarkSceneDirty(UnityEngine.SceneManagement.SceneManager.GetActiveScene());
            Debug.Log("[Marte] World (streaming), water, player and fog created.");
        }

        static void CreateWorld(JezeroWorldInfo info, Transform player)
        {
            var world = new GameObject("World");
            world.SetActive(false);
            var streamer = world.AddComponent<TerrainStreamer>();
            var so = new SerializedObject(streamer);
            so.FindProperty("world").objectReferenceValue = info;
            so.FindProperty("target").objectReferenceValue = player;
            so.ApplyModifiedPropertiesWithoutUndo();
            world.SetActive(true);
        }

        static readonly Color DustColor = new Color(0.89f, 0.77f, 0.60f);   // D12 horizon #E3C49A

        static void CreateLandmarks(JezeroWorldInfo info)
        {
            var go = new GameObject("Landmarks");
            go.SetActive(false);
            var so = new SerializedObject(go.AddComponent<LandmarkMarkers>());
            so.FindProperty("world").objectReferenceValue = info;
            so.ApplyModifiedPropertiesWithoutUndo();
            go.SetActive(true);
        }

        // Mars dust haze (D12). Also hides the switch between full tiles, horizon and backdrop.
        static void SetupFog()
        {
            RenderSettings.fog = true;
            RenderSettings.fogMode = FogMode.Exponential;
            RenderSettings.fogDensity = 0.00012f;
            RenderSettings.fogColor = DustColor;
            RenderSettings.skybox = EnsureMarsSky();
            RenderSettings.ambientMode = AmbientMode.Skybox;
            DynamicGI.UpdateEnvironment();
        }

        // Caramel sky (D12); below the horizon it matches the dust so the world edge never shows.
        static Material EnsureMarsSky()
        {
            const string path = "Assets/Materials/MarsSky.mat";
            var shader = Shader.Find("Marte/Sky Gradient");
            var mat = AssetDatabase.LoadAssetAtPath<Material>(path);
            if (mat == null)
            {
                Directory.CreateDirectory(Path.Combine(Application.dataPath, "Materials"));
                mat = new Material(shader);
                AssetDatabase.CreateAsset(mat, path);
            }
            mat.shader = shader;
            mat.SetColor("_HorizonColor", DustColor);
            mat.SetColor("_GroundColor", DustColor);
            EditorUtility.SetDirty(mat);
            return mat;
        }

        static void Replace(string name)
        {
            var go = GameObject.Find(name);
            if (go != null) Object.DestroyImmediate(go);
        }

        static void CreateWater(JezeroMetadata meta, JezeroWorldInfo info)
        {
            const string matPath = "Assets/Materials/Water.mat";
            var mat = AssetDatabase.LoadAssetAtPath<Material>(matPath);
            if (mat == null)
            {
                Directory.CreateDirectory(Path.Combine(Application.dataPath, "Materials"));
                mat = new Material(Shader.Find("Universal Render Pipeline/Lit"));
                mat.SetColor("_BaseColor", new Color(0.114f, 0.416f, 0.525f));
                mat.SetFloat("_Smoothness", 0.9f);
                AssetDatabase.CreateAsset(mat, matPath);
            }

            // Unity's plane primitive is 10 m wide at scale 1. Covers the backdrop too, so the crater lake
            // continues past the playable edge (it only shows where the terrain is below the water level).
            float scale = Mathf.Max(Mathf.Max(meta.grade.tamanho_x_m, meta.grade.tamanho_z_m), 2f * info.backdropHalfExtent) / 10f;
            var water = GameObject.CreatePrimitive(PrimitiveType.Plane);
            water.name = "Water";
            water.transform.position = new Vector3(0f, meta.agua.y_mundo_com_exagero, 0f);
            water.transform.localScale = new Vector3(scale, 1f, scale);
            water.GetComponent<MeshRenderer>().sharedMaterial = mat;
            water.GetComponent<MeshRenderer>().shadowCastingMode = ShadowCastingMode.Off;
            Object.DestroyImmediate(water.GetComponent<MeshCollider>());
        }

        static GameObject CreatePlayer(JezeroMetadata meta, JezeroWorldInfo info)
        {
            Vector3 start = meta.StartWorld;
            var player = new GameObject("Player");
            player.transform.position = new Vector3(start.x, start.y + 1.1f, start.z);
            player.transform.rotation = Quaternion.Euler(0f, info.startYaw, 0f);

            var controller = player.AddComponent<CharacterController>();
            controller.height = 1.8f;
            controller.radius = 0.35f;
            controller.center = Vector3.zero;

            var pivot = new GameObject("CameraPivot");
            pivot.transform.SetParent(player.transform, false);
            // Eyes 1.75 m above the feet (capsule is 1.8 m, centred on the transform).
            pivot.transform.localPosition = new Vector3(0f, 0.85f, 0f);

            var cameraGo = new GameObject("Main Camera") { tag = "MainCamera" };
            cameraGo.transform.SetParent(pivot.transform, false);
            var cam = cameraGo.AddComponent<Camera>();
            cam.nearClipPlane = 0.1f;
            // See to the edge of the backdrop (the dust fog has hidden it by then).
            cam.farClipPlane = Mathf.Max(Mathf.Max(meta.grade.tamanho_x_m, meta.grade.tamanho_z_m), info.backdropHalfExtent) * 1.5f;
            cameraGo.AddComponent<AudioListener>();

            var fpc = player.AddComponent<FirstPersonController>();
            var so = new SerializedObject(fpc);
            so.FindProperty("cameraPivot").objectReferenceValue = pivot.transform;
            so.ApplyModifiedPropertiesWithoutUndo();

            player.AddComponent<FloatingOrigin>();
            var boundary = new SerializedObject(player.AddComponent<MapBoundary>());
            boundary.FindProperty("world").objectReferenceValue = info;
            boundary.ApplyModifiedPropertiesWithoutUndo();
            return player;
        }
    }
}
