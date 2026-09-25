using System.Collections.Generic;
using UnityEngine;
#if UNITY_EDITOR
using UnityEditor;
#endif

namespace Marte.World
{
    // Keeps full-detail terrain tiles loaded around the target and a low-resolution horizon everywhere else.
    // Lives on a root object at the origin: FloatingOrigin shifts it, so child local positions are true map positions.
    // In edit mode it streams around the Scene view camera (objects are DontSave, never written to the scene).
    [ExecuteAlways]
    public class TerrainStreamer : MonoBehaviour
    {
        [SerializeField] JezeroWorldInfo world;
        [SerializeField] Transform target;
        [SerializeField] float loadRadius = 2500f;
        [SerializeField] float unloadRadius = 3200f;
        [SerializeField] float lookAheadSeconds = 4f;
        [SerializeField] float maxLookAhead = 3000f;
        [SerializeField] int maxConcurrentLoads = 2;
        [SerializeField] float pixelError = 8f;
        [SerializeField] float editorLoadRadius = 1500f;

        const int TerrainGroup = 1;

        readonly Dictionary<Vector2Int, Terrain> loaded = new Dictionary<Vector2Int, Terrain>();
        readonly Dictionary<Vector2Int, ResourceRequest> loading = new Dictionary<Vector2Int, ResourceRequest>();
        readonly List<Vector2Int> scratch = new List<Vector2Int>();
        GameObject[,] horizon;
        GameObject backdrop;
        Vector3 lastTargetPos;
        Vector3 velocity;
        bool hasLastPos;

        public int LoadedCount => loaded.Count;

        void OnEnable()
        {
            if (world == null || world.tilesX <= 0 || world.tilesZ <= 0) return;
            BuildHorizon();
#if UNITY_EDITOR
            if (!Application.isPlaying) EditorApplication.update += EditorTick;
#endif
        }

        void OnDisable()
        {
#if UNITY_EDITOR
            EditorApplication.update -= EditorTick;
#endif
            ClearAll();
        }

        void Start()
        {
            if (!Application.isPlaying || world == null || target == null) return;
            // Ground under the player must exist before the first physics step.
            Vector3 p = transform.InverseTransformPoint(target.position);
            foreach (var key in TilesAround(p, p, 1200f))
                if (!loaded.ContainsKey(key)) Spawn(key, Resources.Load<TerrainData>(world.TileResource(key.x, key.y)));
        }

        void Update()
        {
            if (!Application.isPlaying || world == null || target == null) return;
            Vector3 p = transform.InverseTransformPoint(target.position);
            if (hasLastPos && Time.deltaTime > 0f)
                velocity = Vector3.Lerp(velocity, (p - lastTargetPos) / Time.deltaTime, 0.2f);
            lastTargetPos = p;
            hasLastPos = true;

            Vector3 ahead = p + Vector3.ClampMagnitude(new Vector3(velocity.x, 0f, velocity.z) * lookAheadSeconds, maxLookAhead);
            FinishLoads();
            StartLoads(p, ahead, loadRadius);
            Unload(p, ahead);
        }

#if UNITY_EDITOR
        void EditorTick()
        {
            if (this == null || world == null || Application.isPlaying) return;
            var sv = SceneView.lastActiveSceneView;
            if (sv == null || sv.camera == null) return;
            Vector3 p = transform.InverseTransformPoint(sv.camera.transform.position);
            // One synchronous load per tick keeps the editor responsive.
            foreach (var key in TilesAround(p, p, editorLoadRadius))
            {
                if (loaded.ContainsKey(key)) continue;
                Spawn(key, Resources.Load<TerrainData>(world.TileResource(key.x, key.y)));
                break;
            }
            Unload(p, p, editorLoadRadius + 700f);
        }
#endif

        // ---------------------------------------------------------------- loading
        void StartLoads(Vector3 p, Vector3 ahead, float radius)
        {
            foreach (var key in TilesAround(p, ahead, radius))
            {
                if (loading.Count >= maxConcurrentLoads) break;
                if (loaded.ContainsKey(key) || loading.ContainsKey(key)) continue;
                loading[key] = Resources.LoadAsync<TerrainData>(world.TileResource(key.x, key.y));
            }
        }

        void FinishLoads()
        {
            scratch.Clear();
            foreach (var kv in loading)
                if (kv.Value.isDone) scratch.Add(kv.Key);
            // Collider creation is the expensive part: one tile per frame.
            if (scratch.Count == 0) return;
            var key = scratch[0];
            var data = loading[key].asset as TerrainData;
            loading.Remove(key);
            if (data != null) Spawn(key, data);
        }

        void Spawn(Vector2Int key, TerrainData data)
        {
            if (data == null) return;
            var go = Terrain.CreateTerrainGameObject(data);
            go.name = $"Jezero_{key.x}_{key.y}";
            go.hideFlags = HideFlags.DontSave;
            go.transform.SetParent(transform, false);
            go.transform.localPosition = world.TileOrigin(key.x, key.y);

            var terrain = go.GetComponent<Terrain>();
            terrain.heightmapPixelError = pixelError;
            terrain.drawInstanced = true;
            terrain.groupingID = TerrainGroup;
            terrain.allowAutoConnect = true;
            loaded[key] = terrain;

            if (horizon != null) horizon[key.x, key.y].SetActive(false);
            Terrain.SetConnectivityDirty();
        }

        void Unload(Vector3 p, Vector3 ahead, float radius = -1f)
        {
            if (radius < 0f) radius = unloadRadius;
            scratch.Clear();
            foreach (var kv in loaded)
                if (DistanceToTile(p, kv.Key) > radius && DistanceToTile(ahead, kv.Key) > radius)
                    scratch.Add(kv.Key);
            foreach (var key in scratch)
            {
                var terrain = loaded[key];
                loaded.Remove(key);
                var data = terrain != null ? terrain.terrainData : null;
                if (terrain != null) DestroySafe(terrain.gameObject);
                if (data != null) Resources.UnloadAsset(data);
                if (horizon != null) horizon[key.x, key.y].SetActive(true);
            }
            if (scratch.Count > 0) Terrain.SetConnectivityDirty();
        }

        // Tiles within radius of p or ahead, nearest first.
        List<Vector2Int> TilesAround(Vector3 p, Vector3 ahead, float radius)
        {
            var result = new List<Vector2Int>();
            float hx = world.HalfX, hz = world.HalfZ, size = world.tileSize;
            float minX = Mathf.Min(p.x, ahead.x) - radius, maxX = Mathf.Max(p.x, ahead.x) + radius;
            float minZ = Mathf.Min(p.z, ahead.z) - radius, maxZ = Mathf.Max(p.z, ahead.z) + radius;
            int x0 = Mathf.Max(0, Mathf.FloorToInt((minX + hx) / size)), x1 = Mathf.Min(world.tilesX - 1, Mathf.FloorToInt((maxX + hx) / size));
            int z0 = Mathf.Max(0, Mathf.FloorToInt((minZ + hz) / size)), z1 = Mathf.Min(world.tilesZ - 1, Mathf.FloorToInt((maxZ + hz) / size));
            for (int x = x0; x <= x1; x++)
            for (int z = z0; z <= z1; z++)
            {
                var key = new Vector2Int(x, z);
                if (DistanceToTile(p, key) <= radius || DistanceToTile(ahead, key) <= radius) result.Add(key);
            }
            result.Sort((a, b) => DistanceToTile(p, a).CompareTo(DistanceToTile(p, b)));
            return result;
        }

        float DistanceToTile(Vector3 p, Vector2Int key)
        {
            Vector3 o = world.TileOrigin(key.x, key.y);
            float dx = Mathf.Max(o.x - p.x, 0f, p.x - (o.x + world.tileSize));
            float dz = Mathf.Max(o.z - p.z, 0f, p.z - (o.z + world.tileSize));
            return Mathf.Sqrt(dx * dx + dz * dz);
        }

        // ---------------------------------------------------------------- horizon
        void BuildHorizon()
        {
            var grid = HorizonBuilder.LoadGrid(world.horizonResource, world.HorizonSizeX, world.HorizonSizeZ);
            if (grid == null)
            {
                Debug.LogWarning("[Marte] Horizon grid not found. Run Marte/Terrain/Import Jezero.");
                return;
            }
            var parent = NewChild("Horizon", transform, Vector3.zero);
            horizon = new GameObject[world.tilesX, world.tilesZ];
            for (int x = 0; x < world.tilesX; x++)
            for (int z = 0; z < world.tilesZ; z++)
                horizon[x, z] = NewMeshObject($"Horizon_{x}_{z}", parent.transform, world.TileOrigin(x, z),
                                              HorizonBuilder.BuildHorizonChunk(world, grid, x, z));
            BuildBackdrop();
        }

        void BuildBackdrop()
        {
            if (world.backdropSamples <= 0) return;
            var grid = HorizonBuilder.LoadGrid(world.backdropResource, world.backdropSamples, world.backdropSamples);
            if (grid == null) return;
            backdrop = NewChild("Backdrop", transform, Vector3.zero);
            int chunks = HorizonBuilder.BackdropChunksPerSide(world);
            for (int cx = 0; cx < chunks; cx++)
            for (int cz = 0; cz < chunks; cz++)
            {
                var mesh = HorizonBuilder.BuildBackdropChunk(world, grid, cx, cz);
                if (mesh == null) continue;
                NewMeshObject($"Backdrop_{cx}_{cz}", backdrop.transform, HorizonBuilder.BackdropChunkOrigin(world, cx, cz), mesh);
            }
        }

        static GameObject NewChild(string name, Transform parent, Vector3 localPosition)
        {
            var go = new GameObject(name) { hideFlags = HideFlags.DontSave };
            go.transform.SetParent(parent, false);
            go.transform.localPosition = localPosition;
            return go;
        }

        GameObject NewMeshObject(string name, Transform parent, Vector3 localPosition, Mesh mesh)
        {
            var go = NewChild(name, parent, localPosition);
            go.AddComponent<MeshFilter>().sharedMesh = mesh;
            var mr = go.AddComponent<MeshRenderer>();
            mr.sharedMaterial = world.horizonMaterial;
            mr.shadowCastingMode = UnityEngine.Rendering.ShadowCastingMode.Off;
            mr.receiveShadows = false;
            return go;
        }

        void ClearAll()
        {
            foreach (var kv in loading)
                if (kv.Value.isDone && kv.Value.asset != null) Resources.UnloadAsset(kv.Value.asset);
            loading.Clear();
            foreach (var kv in loaded)
            {
                if (kv.Value == null) continue;
                var data = kv.Value.terrainData;
                DestroySafe(kv.Value.gameObject);
                if (data != null) Resources.UnloadAsset(data);
            }
            loaded.Clear();
            if (horizon != null)
            {
                DestroyMeshTree(horizon[0, 0] != null ? horizon[0, 0].transform.parent.gameObject : null);
                horizon = null;
            }
            DestroyMeshTree(backdrop);
            backdrop = null;
            hasLastPos = false;
        }

        static void DestroyMeshTree(GameObject root)
        {
            if (root == null) return;
            foreach (var mf in root.GetComponentsInChildren<MeshFilter>(true))
                if (mf.sharedMesh != null) DestroySafe(mf.sharedMesh);
            DestroySafe(root);
        }

        static void DestroySafe(Object o)
        {
            if (o == null) return;
            if (Application.isPlaying) Destroy(o); else DestroyImmediate(o);
        }
    }
}
