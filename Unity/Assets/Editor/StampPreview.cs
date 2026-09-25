using System.Globalization;
using System.IO;
using UnityEditor;
using UnityEngine;

namespace Marte.EditorTools
{
    // Renders candidate relief stamps (ferramentas/terreno/cache/stamps/*.raw) so they can be compared in-engine.
    public static class StampPreview
    {
        const int Resolution = 1025;
        static readonly Vector3 Origin = new Vector3(50000f, 0f, 50000f);

        static string Folder =>
            Path.GetFullPath(Path.Combine(Application.dataPath, "..", "..", "ferramentas", "terreno", "cache", "stamps"));

        [MenuItem("Marte/Terrain/Render Stamp Previews")]
        public static void RenderAll()
        {
            var layer = new TerrainLayer { diffuseTexture = MarsTexture(), tileSize = new Vector2(40f, 40f) };
            foreach (var raw in Directory.GetFiles(Folder, "*.raw"))
            {
                string key = Path.GetFileNameWithoutExtension(raw);
                string[] meta = File.ReadAllText(Path.Combine(Folder, key + ".txt")).Split(' ');
                float relief = float.Parse(meta[0], CultureInfo.InvariantCulture);
                float size = float.Parse(meta[1], CultureInfo.InvariantCulture);
                Render(key, raw, relief, size, layer);
            }
            Debug.Log($"[Marte] Stamp previews written to {Folder}");
        }

        static void Render(string key, string rawPath, float relief, float size, TerrainLayer layer)
        {
            var data = new TerrainData { heightmapResolution = Resolution };
            data.size = new Vector3(size, relief, size);
            byte[] bytes = File.ReadAllBytes(rawPath);
            var heights = new float[Resolution, Resolution];
            for (int i = 0, n = 0; i < Resolution; i++)
            for (int j = 0; j < Resolution; j++, n += 2)
                heights[i, j] = (bytes[n] | bytes[n + 1] << 8) / 65535f;
            data.SetHeights(0, 0, heights);
            data.terrainLayers = new[] { layer };

            var go = Terrain.CreateTerrainGameObject(data);
            go.transform.position = Origin;
            var terrain = go.GetComponent<Terrain>();
            terrain.heightmapPixelError = 1f;

            Vector2 wallUv = SteepestSpot(data, out Vector3 downhill);
            Vector3 wall = WorldAt(terrain, wallUv);

            var camGo = new GameObject("StampCam");
            var cam = camGo.AddComponent<Camera>();
            cam.fieldOfView = 55f;
            cam.farClipPlane = 6000f;
            try
            {
                Shoot(cam, terrain, wall, downhill, 650f, 25f, Path.Combine(Folder, $"render_{key}_1.png"));
                Vector3 side = Quaternion.Euler(0f, 55f, 0f) * downhill;
                Shoot(cam, terrain, wall, side, 1100f, 250f, Path.Combine(Folder, $"render_{key}_2.png"));
            }
            finally
            {
                Object.DestroyImmediate(camGo);
                Object.DestroyImmediate(go);
            }
        }

        static void Shoot(Camera cam, Terrain terrain, Vector3 target, Vector3 dir, float dist, float heightAboveGround, string path)
        {
            Vector3 pos = target + dir * dist;
            pos.y = terrain.SampleHeight(pos) + terrain.transform.position.y + heightAboveGround;
            cam.transform.position = pos;
            cam.transform.LookAt(target);

            var rt = new RenderTexture(1280, 720, 24);
            cam.targetTexture = rt;
            cam.Render();
            RenderTexture.active = rt;
            var tex = new Texture2D(1280, 720, TextureFormat.RGB24, false);
            tex.ReadPixels(new Rect(0, 0, 1280, 720), 0, 0);
            tex.Apply();
            File.WriteAllBytes(path, tex.EncodeToPNG());
            RenderTexture.active = null;
            cam.targetTexture = null;
            Object.DestroyImmediate(rt);
            Object.DestroyImmediate(tex);
        }

        // Center of the steepest 7x7 neighbourhood on a 96x96 grid, avoiding the borders.
        static Vector2 SteepestSpot(TerrainData data, out Vector3 downhill)
        {
            const int n = 96;
            var s = new float[n, n];
            for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                s[i, j] = data.GetSteepness(j / (n - 1f), i / (n - 1f));

            float best = -1f; int bi = n / 2, bj = n / 2;
            for (int i = 12; i < n - 12; i++)
            for (int j = 12; j < n - 12; j++)
            {
                float sum = 0f;
                for (int a = -3; a <= 3; a++)
                for (int b = -3; b <= 3; b++) sum += s[i + a, j + b];
                if (sum > best) { best = sum; bi = i; bj = j; }
            }

            Vector2 uv = new Vector2(bj / (n - 1f), bi / (n - 1f));
            Vector3 normal = data.GetInterpolatedNormal(uv.x, uv.y);
            downhill = new Vector3(normal.x, 0f, normal.z).normalized;
            if (downhill.sqrMagnitude < 0.01f) downhill = Vector3.forward;
            return uv;
        }

        static Vector3 WorldAt(Terrain terrain, Vector2 uv)
        {
            var size = terrain.terrainData.size;
            var p = terrain.transform.position + new Vector3(uv.x * size.x, 0f, uv.y * size.z);
            p.y = terrain.SampleHeight(p) + terrain.transform.position.y;
            return p;
        }

        static Texture2D MarsTexture()
        {
            const int n = 256;
            var tex = new Texture2D(n, n, TextureFormat.RGB24, true) { wrapMode = TextureWrapMode.Repeat };
            var baseColor = new Color(0.72f, 0.52f, 0.34f);
            for (int y = 0; y < n; y++)
            for (int x = 0; x < n; x++)
            {
                float v = Mathf.PerlinNoise(x * 0.05f, y * 0.05f) * 0.15f + Mathf.PerlinNoise(x * 0.3f, y * 0.3f) * 0.08f;
                tex.SetPixel(x, y, baseColor * (0.88f + v));
            }
            tex.Apply();
            return tex;
        }
    }
}
