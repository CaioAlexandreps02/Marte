using System;
using UnityEngine;
using UnityEngine.Rendering;

namespace Marte.World
{
    // Builds low-resolution terrain meshes from height grids:
    //  - horizon: one chunk per playable tile (hidden when the full tile is loaded)
    //  - backdrop: large chunks around the map (visual only); cells inside the map rectangle are left out
    // Every chunk has a skirt hanging below its border so no gap shows against a neighbour of different detail.
    public static class HorizonBuilder
    {
        const float SkirtDepth = 40f;
        public const int BackdropChunkCells = 125;

        public static ushort[] LoadGrid(string resource, int sizeX, int sizeZ)
        {
            var asset = Resources.Load<TextAsset>(resource);
            if (asset == null) return null;
            byte[] bytes = asset.bytes;
            if (bytes.Length != sizeX * sizeZ * 2)
                throw new InvalidOperationException($"[Marte] {resource} has {bytes.Length} bytes, expected {sizeX * sizeZ * 2}.");
            var grid = new ushort[sizeX * sizeZ];
            Buffer.BlockCopy(bytes, 0, grid, 0, bytes.Length);
            Resources.UnloadAsset(asset);
            return grid;
        }

        public static Mesh BuildHorizonChunk(JezeroWorldInfo world, ushort[] grid, int tx, int tz)
        {
            int sx = world.HorizonSizeX, sz = world.HorizonSizeZ;
            float scale = world.terrainHeight / 65535f;
            float H(int gx, int gz) => grid[Mathf.Clamp(gz, 0, sz - 1) * sx + Mathf.Clamp(gx, 0, sx - 1)] * scale;
            return BuildChunk($"Horizon_{tx}_{tz}", H, tx * world.horizonStep, tz * world.horizonStep, world.horizonStep,
                              world.tileSize / world.horizonStep, world.TileOrigin(tx, tz), 40f, null);
        }

        public static int BackdropChunksPerSide(JezeroWorldInfo world) => (world.backdropSamples - 1) / BackdropChunkCells;

        public static Vector3 BackdropChunkOrigin(JezeroWorldInfo world, int cx, int cz) =>
            new Vector3(-world.backdropHalfExtent + cx * BackdropChunkCells * world.backdropSpacing, 0f,
                        -world.backdropHalfExtent + cz * BackdropChunkCells * world.backdropSpacing);

        // Returns null when every cell of the chunk is inside the map (tiles/horizon cover it).
        public static Mesh BuildBackdropChunk(JezeroWorldInfo world, ushort[] grid, int cx, int cz)
        {
            int size = world.backdropSamples;
            float H(int gx, int gz) => world.backdropBaseY + grid[Mathf.Clamp(gz, 0, size - 1) * size + Mathf.Clamp(gx, 0, size - 1)] * world.backdropHeightScale;
            Vector3 origin = BackdropChunkOrigin(world, cx, cz);
            float cell = world.backdropSpacing, hx = world.HalfX, hz = world.HalfZ;
            bool CellInsideMap(int i, int j)
            {
                float x = origin.x + (i + 0.5f) * cell, z = origin.z + (j + 0.5f) * cell;
                return x > -hx && x < hx && z > -hz && z < hz;
            }
            bool any = false;
            for (int j = 0; j < BackdropChunkCells && !any; j++)
            for (int i = 0; i < BackdropChunkCells && !any; i++)
                any = !CellInsideMap(i, j);
            if (!any) return null;
            return BuildChunk($"Backdrop_{cx}_{cz}", H, cx * BackdropChunkCells, cz * BackdropChunkCells, BackdropChunkCells,
                              cell, origin, 200f, CellInsideMap);
        }

        // Grid chunk of `cells` x `cells` starting at grid sample (gx0, gz0), with a skirt ring.
        // `skipCell(i, j)` (optional) leaves grid cell (i, j) out of the surface.
        static Mesh BuildChunk(string name, Func<int, int, float> H, int gx0, int gz0, int cells, float cell, Vector3 origin,
                               float uvSize, Func<int, int, bool> skipCell)
        {
            int side = cells + 3;
            var vertices = new Vector3[side * side];
            var normals = new Vector3[side * side];
            var uvs = new Vector2[side * side];

            for (int j = 0; j < side; j++)
            for (int i = 0; i < side; i++)
            {
                int ci = Mathf.Clamp(i - 1, 0, cells);
                int cj = Mathf.Clamp(j - 1, 0, cells);
                int gx = gx0 + ci, gz = gz0 + cj;
                bool skirt = ci != i - 1 || cj != j - 1;

                int v = j * side + i;
                vertices[v] = new Vector3(ci * cell, H(gx, gz) - (skirt ? SkirtDepth : 0f), cj * cell);
                // Normals from the global grid so shading is continuous across chunks.
                normals[v] = new Vector3(H(gx - 1, gz) - H(gx + 1, gz), 2f * cell, H(gx, gz - 1) - H(gx, gz + 1)).normalized;
                uvs[v] = new Vector2((origin.x + ci * cell) / uvSize, (origin.z + cj * cell) / uvSize);
            }

            var triangles = new System.Collections.Generic.List<int>((side - 1) * (side - 1) * 6);
            for (int j = 0; j < side - 1; j++)
            for (int i = 0; i < side - 1; i++)
            {
                // Quad (i, j) of the vertex grid is surface cell (i-1, j-1); skirt quads keep their own index.
                if (skipCell != null && i >= 1 && j >= 1 && i <= cells && j <= cells && skipCell(i - 1, j - 1)) continue;
                int a = j * side + i, b = a + 1, c = a + side, d = c + 1;
                triangles.Add(a); triangles.Add(c); triangles.Add(b);
                triangles.Add(b); triangles.Add(c); triangles.Add(d);
            }

            var mesh = new Mesh { name = name, indexFormat = side * side > 65535 ? IndexFormat.UInt32 : IndexFormat.UInt16 };
            mesh.vertices = vertices;
            mesh.normals = normals;
            mesh.uv = uvs;
            mesh.SetTriangles(triangles, 0);
            mesh.RecalculateBounds();
            return mesh;
        }
    }
}
