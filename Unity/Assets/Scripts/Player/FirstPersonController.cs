using UnityEngine;
using UnityEngine.InputSystem;

namespace Marte.Player
{
    [RequireComponent(typeof(CharacterController))]
    public class FirstPersonController : MonoBehaviour
    {
        [SerializeField] Transform cameraPivot;
        [SerializeField] float walkSpeed = 5f;
        [SerializeField] float runSpeed = 60f;
        [SerializeField] float jumpHeight = 1.2f;
        [SerializeField] float gravity = 9.81f;
        [SerializeField] float mouseSensitivity = 0.1f;

        [Header("Fly mode (F) - map exploration")]
        [SerializeField] float flySpeed = 80f;
        [SerializeField] float flyFastSpeed = 400f;

        CharacterController controller;
        float verticalVelocity;
        float pitch;
        bool flying;

        void Awake()
        {
            controller = GetComponent<CharacterController>();
            LockCursor(true);
        }

        void Update()
        {
            var keyboard = Keyboard.current;
            var mouse = Mouse.current;
            if (keyboard == null || mouse == null) return;

            if (keyboard.escapeKey.wasPressedThisFrame) LockCursor(false);
            else if (mouse.leftButton.wasPressedThisFrame && Cursor.lockState != CursorLockMode.Locked) LockCursor(true);

            if (keyboard.fKey.wasPressedThisFrame)
            {
                flying = !flying;
                verticalVelocity = 0f;
            }

            if (Cursor.lockState == CursorLockMode.Locked)
            {
                Vector2 look = mouse.delta.ReadValue() * mouseSensitivity;
                transform.Rotate(0f, look.x, 0f);
                pitch = Mathf.Clamp(pitch - look.y, -89f, 89f);
                cameraPivot.localRotation = Quaternion.Euler(pitch, 0f, 0f);
            }

            float x = (keyboard.dKey.isPressed ? 1f : 0f) - (keyboard.aKey.isPressed ? 1f : 0f);
            float z = (keyboard.wKey.isPressed ? 1f : 0f) - (keyboard.sKey.isPressed ? 1f : 0f);
            bool fast = keyboard.leftShiftKey.isPressed;

            if (flying)
            {
                float y = (keyboard.spaceKey.isPressed ? 1f : 0f) - (keyboard.leftCtrlKey.isPressed ? 1f : 0f);
                Vector3 dir = cameraPivot.right * x + cameraPivot.forward * z + Vector3.up * y;
                controller.Move(Vector3.ClampMagnitude(dir, 1f) * (fast ? flyFastSpeed : flySpeed) * Time.deltaTime);
                return;
            }

            float speed = fast ? runSpeed : walkSpeed;
            Vector3 move = Vector3.ClampMagnitude(transform.right * x + transform.forward * z, 1f) * speed;

            if (controller.isGrounded && verticalVelocity < 0f) verticalVelocity = -2f;
            if (controller.isGrounded && keyboard.spaceKey.wasPressedThisFrame)
                verticalVelocity = Mathf.Sqrt(2f * gravity * jumpHeight);
            verticalVelocity -= gravity * Time.deltaTime;

            move.y = verticalVelocity;
            controller.Move(move * Time.deltaTime);
        }

        static void LockCursor(bool locked)
        {
            Cursor.lockState = locked ? CursorLockMode.Locked : CursorLockMode.None;
            Cursor.visible = !locked;
        }
    }
}
