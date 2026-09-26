using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Text.RegularExpressions;
using UnityEngine;

namespace Marte.EditorTools
{
    // Mirror of ferramentas/terreno/saida/metadata.json (only the fields Unity needs).
    [Serializable]
    public class JezeroMetadata
    {
        [Serializable] public class Grid { public int tiles_x, tiles_z; public float tamanho_tile_m; public int amostras_por_tile; public float tamanho_x_m, tamanho_z_m; }
        [Serializable] public class Size { public float x, y, z; }
        [Serializable] public class UnityInfo { public Size terrain_size; public int heightmap_resolution; public float exagero_vertical; }
        [Serializable] public class Water { public float nivel_m; public float y_mundo_com_exagero; }
        [Serializable] public class Start { public float x_m, z_m; public float y_mundo_com_exagero; }
        [Serializable] public class Height { public float min_codificado_m; public float faixa_m; }
        [Serializable] public class Backdrop { public string arquivo; public int amostras; public float espacamento_m, meia_largura_m, min_codificado_m, faixa_m; }
        [Serializable] public class Reference { public float desloc_x_m, desloc_z_m; }

        // ferramentas/terreno/marcos.json (reference-frame km coordinates).
        [Serializable] public class Marco { public string id; public int numero; public string nome, tipo, origem, caverna, gelo, descricao; public float x_km, z_km; public bool visivel_de_longe; }
        [Serializable] public class MarcoList { public Marco[] marcos; }

        public Grid grade;
        public Reference referencia;
        public Height altura;
        public UnityInfo unity;
        public Water agua;
        public Start inicio_jogador;
        public Backdrop fundo;

        [NonSerialized] public Vector2[] playableArea;

        public static string Folder =>
            Path.GetFullPath(Path.Combine(Application.dataPath, "..", "..", "ferramentas", "terreno", "saida"));

        public static JezeroMetadata Load()
        {
            string path = Path.Combine(Folder, "metadata.json");
            if (!File.Exists(path))
                throw new FileNotFoundException($"[Marte] {path} not found. Run ferramentas/terreno/exportar_heightmap.py first.");
            string json = File.ReadAllText(path);
            var meta = JsonUtility.FromJson<JezeroMetadata>(json);
            meta.playableArea = ParsePolygon(json, "poligono_m_centro");
            return meta;
        }

        // JsonUtility cannot read nested arrays: pull the [[x, z], ...] list out by hand.
        static Vector2[] ParsePolygon(string json, string key)
        {
            int k = json.IndexOf($"\"{key}\"", StringComparison.Ordinal);
            if (k < 0) return Array.Empty<Vector2>();
            int open = json.IndexOf('[', k), depth = 0, end = open;
            for (; end < json.Length; end++)
            {
                if (json[end] == '[') depth++;
                else if (json[end] == ']' && --depth == 0) break;
            }
            var nums = new List<float>();
            foreach (Match m in Regex.Matches(json.Substring(open, end - open), @"-?\d+(\.\d+)?([eE][-+]?\d+)?"))
                nums.Add(float.Parse(m.Value, CultureInfo.InvariantCulture));
            var poly = new Vector2[nums.Count / 2];
            for (int i = 0; i < poly.Length; i++) poly[i] = new Vector2(nums[2 * i], nums[2 * i + 1]);
            return poly;
        }

        public static Marco[] LoadMarcos()
        {
            string path = Path.Combine(Folder, "..", "marcos.json");
            return File.Exists(path) ? JsonUtility.FromJson<MarcoList>(File.ReadAllText(path)).marcos ?? Array.Empty<Marco>() : Array.Empty<Marco>();
        }

        // Reference-frame km (edicoes/marcos) -> true position with the origin at the map center (y = 0).
        public Vector3 ReferenceToWorld(float xKm, float zKm) =>
            new Vector3(xKm * 1000f + referencia.desloc_x_m - HalfX, 0f, zKm * 1000f + referencia.desloc_z_m - HalfZ);

        public float HalfX => grade.tamanho_x_m / 2f;
        public float HalfZ => grade.tamanho_z_m / 2f;
        public Vector3 StartWorld => new Vector3(inicio_jogador.x_m - HalfX, inicio_jogador.y_mundo_com_exagero, inicio_jogador.z_m - HalfZ);
    }
}
