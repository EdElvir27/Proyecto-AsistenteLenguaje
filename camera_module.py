import cv2

def initialize_camera(width=1920, height=1080, fps=30):
      # Capturar video desde la cámara y establecer resolución alta
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cap.set(cv2.CAP_PROP_FPS, fps)

    # Ajustar el balance de blancos automáticamente
    cap.set(cv2.CAP_PROP_AUTO_WB, 0)  #Desactivar balance de blancos automático
    cap.set(cv2.CAP_PROP_WB_TEMPERATURE, 4500)

    if not cap.isOpened():
        print("Error: No se pudo acceder a la cámara.")
        return None

    return cap

def release_camera(cap):
    """Releases the camera and closes all OpenCV windows."""
    if cap is not None:
        cap.release()
    cv2.destroyAllWindows()