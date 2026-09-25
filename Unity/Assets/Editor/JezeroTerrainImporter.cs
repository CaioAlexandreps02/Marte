using System;
using System.IO;
using Marte.World;
using UnityEditor;
using UnityEngine;

namespace Marte.EditorTools
{
    // Converts the RAW tiles from ferramentas/terreno/exportar_heightmap.py into streamable TerrainData assets
    // (Resources/Terrain/Jezero), the whole-map horizon grid and the JezeroWorldInfo asset used by TerrainStreamer.
    public static class JezeroTerrainImporter
    {
        const string ResourcesRoot = "Assets/Resources/Terrain";
        const string TilesFolder = ResourcesRoot + "/Jezero";
        const string HorizonFile = ResourcesRoot + "/JezeroHorizon.bytes";
        const string BackdropFile = ResourcesRoot + "/JezeroBackdrop.bytes";
        public const string WorldInfoPath = ResourcesRoot + "/JezeroWorldInfo.asset";
        const string TexturesFolder = "Assets/Terrain/Textures";
        const int HorizonStep = 32;

        [MenuItem("Marte/Terrain/Import Jezero")]
        public static void Import()
        {
            var meta = JezeroMetadata.Load();
            int tilesX = meta.grade.tiles_x, tilesZ = meta.grade.tiles_z;
            int resolution = meta.unity.heightmap_resolution;
            var size = new Vector3(meta.unity.terrain_size.x, meta.unity.terrain_size.y, meta.unity.terrain_size.z);
            string raw = JezeroMetadata.Folder;

            RemoveLegacy();
            if (AssetDatabase.IsValidFolder(TilesFolder)) AssetDatabase.DeleteAsset(TilesFolder);
            Directory.CreateDirectory(Path.GetFullPath(TilesFolder));
            Directory.CreateDirectory(Path.GetFullPath(TexturesFolder));
            AssetDatabase.Refresh();

            var layer = EnsureGroundLayer();
            var horizonMaterial = EnsureHorizonMaterial(layer.diffuseTexture);

            int hsx = tilesX * HorizonStep + 1, hsz = tilesZ * HorizonStep + 1;
            var horizon = new ushort[hsx * hsz];
            var buffer = new ushort[resolution * resolution];
            int step = (resolution - 1) / HorizonStep;

            try
            {
                int done = 0;
                for (int x = 0; x < tilesX; x++)
                for (int z = 0; z < tilesZ; z++, done++)
                {
                    if (EditorUtility.DisplayCancelableProgressBar("Importing Jezero", $"Tile {x},{z}", done / (float)(tilesX * tilesZ)))
                        throw new OperationCanceledException("Import cancelled.");

                    ReadTile(Path.Combine(raw, $"Jezero_{x}_{z}.raw"), resolution, buffer);

                    // Splat/basemap small until real texturing: saves ~5 MB per tile.
                    var data = new TerrainData { heightmapResolution = resolution, alphamapResolution = 16, baseMapResolution = 16 };
                    data.size = size;
                    data.SetHeights(0, 0, ToHeights(buffer, resolution));
                    data.terrainLayers = new[] { layer };
                    AssetDatabase.CreateAsset(data, $"{TilesFolder}/Jezero_{x}_{z}.asset");

                    for (int r = 0; r <= HorizonStep; r++)
                    for (int c = 0; c <= HorizonStep; c++)
                        horizon[(z * HorizonStep + r) * hsx + x * HorizonStep + c] = buffer[r * step * resolution + c * step];

                    if (done % 25 == 24)
                    {
                        AssetDatabase.SaveAssets();
                        EditorUtility.UnloadUnusedAssetsImmediate();
                    }
                }
            }
            finally
            {
                EditorUtility.ClearProgressBar();
            }

            var bytes = new byte[horizon.Length * 2];
            Buffer.BlockCopy(horizon, 0, bytes, 0, bytes.Length);
            File.WriteAllBytes(Path.GetFullPath(HorizonFile), bytes);
            AssetDatabase.ImportAsset(HorizonFile);

            var info = AssetDatabase.LoadAssetAtPath<JezeroWorldInfo>(WorldInfoPath);
            if (info == null)
            {
                info = ScriptableObject.CreateInstance<JezeroWorldInfo>();
                AssetDatabase.CreateAsset(info, WorldInfoPath);
            }
            info.tilesX = tilesX;
            info.tilesZ = tilesZ;
            info.tileSize = size.x;
            info.terrainHeight = size.y;
            info.horizonStep = HorizonStep;
            info.horizonMaterial = horizonMaterial;
            info.waterY = meta.agua.y_mundo_com_exagero;
            info.start = meta.StartWorld;
            info.playableArea = meta.playableArea;
            ImportBackdrop(meta, info);
            EditorUtility.SetDirty(info);
            AssetDatabase.SaveAssets();
            EditorUtility.UnloadUnusedAssetsImmediate();

            Debug.Log($"[Marte] Jezero imported: {tilesX * tilesZ} streamable tiles ({tilesX}x{tilesZ} km) + horizon {hsx}x{hsz}, playable area {info.playableArea.Length} vertices.");
        }

        [MenuItem("Marte/Terrain/Import Backdrop Only")]
        public static void ImportBackdropOnly()
        {
            var info = AssetDatabase.LoadAssetAtPath<JezeroWorldInfo>(WorldInfoPath);
            if (info == null)
            {
                Debug.LogError("[Marte] Run Marte/Terrain/Import Jezero first.");
                return;
            }
            ImportBackdrop(JezeroMetadata.Load(), info);
            EditorUtility.SetDirty(info);
            AssetDatabase.SaveAssets();
        }

        // Visual-only terrain around the map (ferramentas/terreno/exportar_fundo.py). Same vertical reference as the tiles.
        static void ImportBackdrop(JezeroMetadata meta, JezeroWorldInfo info)
        {
            var f = meta.fundo;
            string src = f != null && !string.IsNullOrEmpty(f.arquivo) ? Path.Combine(JezeroMetadata.Folder, f.arquivo) : null;
            if (src == null || !File.Exists(src))
            {
                info.backdropSamples = 0;
                Debug.LogWarning("[Marte] No backdrop (run ferramentas/terreno/exportar_fundo.py).");
                return;
            }
            File.Copy(src, Path.GetFullPath(BackdropFile), true);
            AssetDatabase.ImportAsset(BackdropFile);
            float ex = meta.unity.exagero_vertical;
            info.backdropSamples = f.amostras;
            info.backdropSpacing = f.espacamento_m;
            info.backdropHalfExtent = f.meia_largura_m;
            info.backdropBaseY = (f.min_codificado_m - meta.altura.min_codificado_m) * ex;
            info.backdropHeightScale = f.faixa_m * ex / 65535f;
            Debug.Log($"[Marte] Backdrop imported: {f.amostras}x{f.amostras} at {f.espacamento_m} m ({2 * f.meia_largura_m / 1000f} km).");
        }

        // Pre-streaming versions put every tile in the scene.
        static void RemoveLegacy()
        {
            var legacy = GameObject.Find("Jezero");
            if (legacy != null) UnityEngine.Object.DestroyImmediate(legacy);
            if (AssetDatabase.IsValidFolder("Assets/Terrain/Jezero")) AssetDatabase.DeleteAsset("Assets/Terrain/Jezero");
        }

        static void ReadTile(string path, int resolution, ushort[] buffer)
        {
            byte[] bytes = File.ReadAllBytes(path);
            if (bytes.Length != resolution * resolution * 2)
                throw new InvalidDataException($"{path}: expected {resolution * resolution * 2} bytes, got {bytes.Length}");
            Buffer.BlockCopy(bytes, 0, buffer, 0, bytes.Length);
        }

        // RAW row 0 = south = z 0, matching Unity's heights[z, x].
        static float[,] ToHeights(ushort[] buffer, int resolution)
        {
            var heights = new float[resolution, resolution];
            for (int row = 0, i = 0; row < resolution; row++)
            for (int col = 0; col < resolution; col++, i++)
                heights[row, col] = buffer[i] / 65535f;
            return heights;
        }

        // Placeholder ground in the D12 Mars palette until the real texturing pass (MicroSplat).
        static TerrainLayer EnsureGroundLayer()
        {
            const string texPath = TexturesFolder + "/MarsGround.png";
            const string layerPath = TexturesFolder + "/MarsGround.terrainlayer";
            if (!File.Exists(Path.GetFullPath(texPath)))
            {
                const int n = 256;
                var tex = new Texture2D(n, n, TextureFormat.RGB24, false);
                var baseColor = new Color(0.725f, 0.525f, 0.341f);
                for (int y = 0; y < n; y++)
                for (int x = 0; x < n; x++)
                {
                    float v = Mathf.PerlinNoise(x * 0.05f, y * 0.05f) * 0.15f + Mathf.PerlinNoise(x * 0.3f, y * 0.3f) * 0.08f;
                    tex.SetPixel(x, y, baseColor * (0.88f + v));
                }
                File.WriteAllBytes(Path.GetFullPath(texPath), tex.EncodeToPNG());
                UnityEngine.Object.DestroyImmediate(tex);
                AssetDatabase.ImportAsset(texPath);
            }
            var layer = AssetDatabase.LoadAssetAtPath<TerrainLayer>(layerPath);
            if (layer == null)
            {
                layer = new TerrainLayer { diffuseTexture = AssetDatabase.LoadAssetAtPath<Texture2D>(texPath), tileSize = new Vector2(40f, 40f) };
                AssetDatabase.CreateAsset(layer, layerPath);
            }
            return layer;
        }

        static Material EnsureHorizonMaterial(Texture2D texture)
        {
            const string matPath = TexturesFolder + "/Horizon.mat";
            var mat = AssetDatabase.LoadAssetAtPath<Material>(matPath);
            if (mat == null)
            {
                mat = new Material(Shader.Find("Universal Render Pipeline/Lit"));
                AssetDatabase.CreateAsset(mat, matPath);
            }
            mat.SetTexture("_BaseMap", texture);
            mat.SetColor("_BaseColor", Color.white);
            mat.SetFloat("_Smoothness", 0.05f);
            EditorUtility.SetDirty(mat);
            return mat;
        }
    }
}
