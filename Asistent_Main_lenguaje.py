import cv2
import mediapipe as mp
import tkinter as tk
from PIL import Image, ImageTk
from camera_module import initialize_camera, release_camera
from gesture_recognition import recognize_gesture

# Inicializar Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)  # Detectar hasta dos manos

# Inicializar la cámara usando el módulo de cámara
cap = initialize_camera()
if cap is None:
    print("Error: No se pudo acceder a la cámara.")
    exit()

# Crear la ventana principal de tkinter
root = tk.Tk()
root.title("Asistente de Lenguaje de Señas")
root.geometry("1000x700")
root.configure(bg='#F0FFFF')

# Crear un label para mostrar el video
camera_label = tk.Label(root)
camera_label.pack(pady=10)

# Crear un botón para cerrar la aplicación
close_button = tk.Button(root, text="Cerrar", command=root.destroy, bg='red', fg='white', font=('Arial', 12, 'bold'))
close_button.pack(pady=10)

# Crear un label para mostrar el gesto reconocido
gesture_label = tk.Label(root, text="", font=('Arial', 20, 'bold'), bg='#F0FFFF')
gesture_label.pack(pady=10)

# Función para actualizar el feed de la cámara
def update_frame():
    ret, frame = cap.read()

    if not ret:
        print("No se pudo capturar el video.")
        return

    # Convertir el frame a RGB y redimensionar para mejorar rendimiento
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (640, 480))

    # Procesar la imagen con Mediapipe
    results = hands.process(frame)

    # Si se detectan manos, dibujar las marcas de la mano en el frame y reconocer el gesto
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = recognize_gesture(hand_landmarks)
            gesture_label.config(text=f"Gesto: {gesture}")
            print(f"Gesto reconocido: {gesture}")
    else:
        gesture_label.config(text="Gesto: desconocido")
        print("No se detectaron manos")

    # Convertir nuevamente el frame a BGR para mostrar con OpenCV y redimensionar para tkinter
    frame_resized = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    frame_resized = cv2.resize(frame_resized, (900, 600))

    # Convertir el frame en un formato que tkinter pueda mostrar
    imgtk = ImageTk.PhotoImage(image=Image.fromarray(frame_resized))
    camera_label.imgtk = imgtk
    camera_label.config(image=imgtk)

    # Programar la próxima actualización
    root.after(10, update_frame)

# Iniciar el ciclo de actualización
update_frame()

# Cerrar las ventanas adecuadamente al cerrar la app
def on_closing():
    release_camera(cap)
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()