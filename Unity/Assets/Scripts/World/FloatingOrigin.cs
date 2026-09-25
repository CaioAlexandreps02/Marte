using UnityEngine;
using UnityEngine.SceneManagement;

namespace Marte.World
{
    // Keeps the tracked object near (0,0,0) by shifting every root object, so float precision
    // stays good anywhere on a 16 km map. True map position = WorldOffset + transform.position.
    public class FloatingOrigin : MonoBehaviour
    {
        [SerializeField] float threshold = 1000f;

        public static double OffsetX { get; private set; }
        public static double OffsetZ { get; private set; }

        public static Vector3 ToTrueWorld(Vector3 local) =>
            new Vector3((float)(local.x + OffsetX), local.y, (float)(local.z + OffsetZ));

        void LateUpdate()
        {
            Vector3 p = transform.position;
            if (p.x * p.x + p.z * p.z < threshold * threshold) return;

            var shift = new Vector3(-p.x, 0f, -p.z);
            foreach (var root in SceneManager.GetActiveScene().GetRootGameObjects())
                root.transform.position += shift;

            OffsetX -= shift.x;
            OffsetZ -= shift.z;
            Physics.SyncTransforms();
        }

        [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.SubsystemRegistration)]
        static void ResetOffset()
        {
            OffsetX = 0;
            OffsetZ = 0;
        }
    }
}
