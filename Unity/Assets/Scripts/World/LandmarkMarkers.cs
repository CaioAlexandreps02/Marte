using UnityEngine;
using UnityEngine.InputSystem;
#if UNITY_EDITOR
using UnityEditor;
#endif

namespace Marte.World
{
    // Placeholder markers for the named places (marcos.json): a coloured pole on the ground plus an on-screen label
    // with the distance. Stand-in until caves, wrecks and props get real models. M cycles labels: near / all / off.
    // Lives on a root object at the origin, like the terrain, so FloatingOrigin keeps it aligned.
    [ExecuteAlways]
    public class LandmarkMarkers : MonoBehaviour
    {
        [SerializeField] JezeroWorldInfo world;
        [SerializeField] float poleHeight = 14f;
        [SerializeField] float nearDistance = 3000f;

        enum LabelMode { Near, All, Off }
        LabelMode mode = LabelMode.Near;
        GameObject poles;
        GUIStyle style;

        void OnEnable()
        {
            if (world == null || world.landmarks == null) return;
            poles = new GameObject("Poles") { hideFlags = HideFlags.DontSave };
            poles.transform.SetParent(transform, false);
            foreach (var l in world.landmarks)
            {
                var pole = GameObject.CreatePrimitive(PrimitiveType.Cylinder);
                pole.name = l.id;
                pole.hideFlags = HideFlags.DontSave;
                DestroySafe(pole.GetComponent<Collider>());
                pole.transform.SetParent(poles.transform, false);
                pole.transform.localPosition = l.position + Vector3.up * poleHeight / 2f;
                pole.transform.localScale = new Vector3(0.6f, poleHeight / 2f, 0.6f);
                var mr = pole.GetComponent<MeshRenderer>();
                mr.sharedMaterial = MaterialFor(l.type);
                mr.shadowCastingMode = UnityEngine.Rendering.ShadowCastingMode.Off;
            }
        }

        void OnDisable()
        {
            if (poles != null)
                foreach (var mr in poles.GetComponentsInChildren<MeshRenderer>(true))
                    DestroySafe(mr.sharedMaterial);
            DestroySafe(poles);
            poles = null;
        }

        void Update()
        {
            if (!Application.isPlaying) return;
            var keyboard = Keyboard.current;
            if (keyboard != null && keyboard.mKey.wasPressedThisFrame)
                mode = (LabelMode)(((int)mode + 1) % 3);
        }

        void OnGUI()
        {
            var cam = Camera.main;
            if (world == null || world.landmarks == null || cam == null || mode == LabelMode.Off) return;
            style ??= new GUIStyle(GUI.skin.box) { fontSize = 13, alignment = TextAnchor.MiddleCenter };
            Vector3 camTrue = transform.InverseTransformPoint(cam.transform.position);

            foreach (var l in world.landmarks)
            {
                float dist = Vector2.Distance(new Vector2(camTrue.x, camTrue.z), new Vector2(l.position.x, l.position.z));
                if (mode == LabelMode.Near && dist > nearDistance) continue;
                Vector3 sp = cam.WorldToScreenPoint(transform.TransformPoint(l.position + Vector3.up * poleHeight));
                if (sp.z <= 0f) continue;
                string label = (l.number > 0 ? $"{l.number}. " : "") + l.name +
                               (dist >= 1000f ? $"  {dist / 1000f:0.0} km" : $"  {dist:0} m");
                var size = style.CalcSize(new GUIContent(label));
                GUI.color = ColorFor(l.type);
                GUI.Box(new Rect(sp.x - size.x / 2f, Screen.height - sp.y - size.y - 4f, size.x + 8f, size.y + 4f), label, style);
            }
            GUI.color = Color.white;
            string help = mode == LabelMode.Near ? $"Marcos: até {nearDistance / 1000f:0} km (M: todos)" : "Marcos: todos (M: esconder)";
            GUI.Label(new Rect(10f, Screen.height - 26f, 360f, 22f), help);
        }

#if UNITY_EDITOR
        void OnDrawGizmos()
        {
            if (world == null || world.landmarks == null) return;
            foreach (var l in world.landmarks)
            {
                Vector3 top = transform.TransformPoint(l.position + Vector3.up * poleHeight);
                Handles.color = ColorFor(l.type);
                Handles.Label(top, (l.number > 0 ? $"{l.number}. " : "") + l.name);
            }
        }
#endif

        static Color ColorFor(string type) => type switch
        {
            "caverna" => new Color(0.55f, 0.85f, 1f),
            "mesa" => new Color(1f, 0.78f, 0.45f),
            "historia" => new Color(1f, 0.55f, 0.55f),
            "recurso" => new Color(0.6f, 1f, 0.6f),
            "mirante" => new Color(0.95f, 0.95f, 0.5f),
            "base" or "inicio" => Color.white,
            _ => new Color(0.85f, 0.75f, 1f),
        };

        static Material MaterialFor(string type)
        {
            var mat = new Material(Shader.Find("Universal Render Pipeline/Lit")) { hideFlags = HideFlags.DontSave };
            Color c = ColorFor(type);
            mat.SetColor("_BaseColor", c);
            mat.EnableKeyword("_EMISSION");
            mat.SetColor("_EmissionColor", c * 0.6f);
            return mat;
        }

        static void DestroySafe(Object o)
        {
            if (o == null) return;
            if (Application.isPlaying) Destroy(o); else DestroyImmediate(o);
        }
    }
}
