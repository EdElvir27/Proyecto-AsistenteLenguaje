import cv2
import mediapipe as mp
import tkinter as tk
from PIL import Image, ImageTk
from camera_module import initialize_camera, release_camera
from gesture_recognition import recognize_gesture

# Inicializar Mediapipe
mp_hands = mp.solutions.hands
# Grado de sensibilidad
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5) 


# Inicializar la cámara usando el módulo de cámara
cap = initialize_camera()
if cap is None:
    print("Error: No se pudo acceder a la cámara.")
    exit()

# Crear la ventana principal de tkinter
root = tk.Tk()
root.title("Asistente de Lenguaje de Señas")
root.geometry("800x600")
root.configure(bg='#F0FFFF')

# Centrar la ventana en la pantalla
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Crear un layout de dos columnas usando grid
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)  # Columna izquierda
root.grid_columnconfigure(1, weight=1)  # Columna derecha (para el video)

# Crear un frame a la izquierda (espacio reservado para futuros componentes)
left_frame = tk.Frame(root, width=300, height=600, bg='#E0E0E0')
left_frame.grid(row=0, column=0, padx=10, pady=10)

# Crear un label para mostrar el video en la columna derecha
camera_label = tk.Label(root)
camera_label.grid(row=0, column=1, padx=10, pady=10, sticky='n')

# Crear un botón para cerrar la aplicación
close_button = tk.Button(root, text="Cerrar", command=root.destroy, bg='#FF6347', fg='white', font=('Arial', 12, 'bold'))
close_button.place(relx=0.9, rely=0.9, anchor='center')

# Crear un label para mostrar el gesto reconocido
gesture_label = tk.Label(root, text="", font=('Arial', 20, 'bold'), bg='#F0FFFF')
gesture_label.grid(row=2, column=1, pady=10)

# Función para actualizar el feed de la cámara
def update_frame():
    ret, frame = cap.read()

    if not ret:
        print("No se pudo capturar el video.")
        return
     # Voltear el frame horizontalmente (para que no se vea como espejo)
    frame = cv2.flip(frame, 1)  # Voltea el frame horizontalmente
    
    # Convertir el frame a RGB y redimensionar
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

    # Convertir nuevamente el frame a BGR para mostrar con OpenCV
    frame_resized = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

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