using UnityEngine;

namespace Marte.World
{
    // Keeps the player inside the playable area: the map rectangle (minus a margin) and the playable polygon
    // (e.g. halfway up the crater rim). Near a limit the suit warns that the base signal is weak; at the limit the
    // player slides along it. The visual-only terrain continues beyond, so the world never "ends".
    // Runs before FloatingOrigin so the shift always sees the corrected position.
    [DefaultExecutionOrder(-100)]
    public class MapBoundary : MonoBehaviour
    {
        [SerializeField] JezeroWorldInfo world;
        [SerializeField] float hardMargin = 300f;
        [SerializeField] float warnDistance = 900f;

        Vector2 lastValid;
        bool hasLastValid;
        bool atLimit;
        float distanceToLimit = float.MaxValue;
        GUIStyle style;

        void LateUpdate()
        {
            if (world == null) return;
            Vector3 local = transform.position;
            Vector3 t = FloatingOrigin.ToTrueWorld(local);
            var p = new Vector2(t.x, t.z);

            if (!hasLastValid || IsValid(p))
            {
                lastValid = p;
                hasLastValid = true;
                atLimit = false;
            }
            else
            {
                // Keep the movement along the limit instead of stopping dead.
                var slideX = new Vector2(p.x, lastValid.y);
                var slideZ = new Vector2(lastValid.x, p.y);
                Vector2 target = IsValid(slideX) ? slideX : IsValid(slideZ) ? slideZ : lastValid;
                transform.position = new Vector3(local.x + (target.x - p.x), local.y, local.z + (target.y - p.y));
                Physics.SyncTransforms();
                lastValid = target;
                p = target;
                atLimit = true;
            }
            distanceToLimit = DistanceToLimit(p);
        }

        bool IsValid(Vector2 p)
        {
            float hx = world.HalfX - hardMargin, hz = world.HalfZ - hardMargin;
            if (p.x < -hx || p.x > hx || p.y < -hz || p.y > hz) return false;
            var poly = world.playableArea;
            return poly == null || poly.Length < 3 || Inside(poly, p);
        }

        float DistanceToLimit(Vector2 p)
        {
            float d = Mathf.Min(world.HalfX - hardMargin - Mathf.Abs(p.x), world.HalfZ - hardMargin - Mathf.Abs(p.y));
            var poly = world.playableArea;
            if (poly != null && poly.Length >= 3)
                for (int i = 0, j = poly.Length - 1; i < poly.Length; j = i++)
                    d = Mathf.Min(d, DistanceToSegment(p, poly[j], poly[i]));
            return Mathf.Max(0f, d);
        }

        static bool Inside(Vector2[] poly, Vector2 p)
        {
            bool inside = false;
            for (int i = 0, j = poly.Length - 1; i < poly.Length; j = i++)
                if ((poly[i].y > p.y) != (poly[j].y > p.y) &&
                    p.x < (poly[j].x - poly[i].x) * (p.y - poly[i].y) / (poly[j].y - poly[i].y) + poly[i].x)
                    inside = !inside;
            return inside;
        }

        static float DistanceToSegment(Vector2 p, Vector2 a, Vector2 b)
        {
            Vector2 ab = b - a;
            float t = Mathf.Clamp01(Vector2.Dot(p - a, ab) / Mathf.Max(ab.sqrMagnitude, 1e-6f));
            return Vector2.Distance(p, a + t * ab);
        }

        void OnGUI()
        {
            if (distanceToLimit > warnDistance && !atLimit) return;
            style ??= new GUIStyle(GUI.skin.box) { fontSize = 20, alignment = TextAnchor.MiddleCenter, wordWrap = true };
            float strength = 1f - distanceToLimit / warnDistance;
            GUI.color = new Color(1f, 0.76f, 0.28f, 0.6f + 0.4f * strength);
            string text = atLimit
                ? "LIMITE DO SINAL DA BASE\nNão é possível seguir adiante. Retorne."
                : $"SINAL DA BASE FRACO\nFora da área de operação em {distanceToLimit:0} m. Retorne.";
            GUI.Box(new Rect(Screen.width / 2f - 260f, 40f, 520f, 70f), text, style);
            GUI.color = Color.white;
        }
    }
}
