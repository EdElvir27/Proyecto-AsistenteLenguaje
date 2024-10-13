import mediapipe as mp

# Inicializar Mediapipe
mp_hands = mp.solutions.hands

def recognize_gesture(hand_landmarks):
    """
    esta funcion va a reconocer el gesto de la mano(piedra, papel, tijera) basado en los puntos de referencia de la mano.
    Parametros: hand_landmarks (NormalizedLandmarkList): Lista de puntos de referencia de la mano.
       Returns:
        str: El gesto reconocido ('piedra', 'papel', 'tijera' o 'desconocido').
    """
    # Obtener las coordenadas de los puntos de referencia relevantes
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]#pulgar
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]#indice
    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]#medio
    ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]#anular
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]#pequeño

    # Calcular distancias entre los puntos de referencia
    thumb_index_dist = abs(thumb_tip.x - index_tip.x) + abs(thumb_tip.y - index_tip.y)
    index_middle_dist = abs(index_tip.x - middle_tip.x) + abs(index_tip.y - middle_tip.y)
    middle_ring_dist = abs(middle_tip.x - ring_tip.x) + abs(middle_tip.y - ring_tip.y)
    ring_pinky_dist = abs(ring_tip.x - pinky_tip.x) + abs(ring_tip.y - pinky_tip.y)

    # Determinar el gesto basado en las distancias
    if thumb_index_dist < 0.1 and index_middle_dist < 0.1 and middle_ring_dist < 0.1 and ring_pinky_dist < 0.1:
        return 'piedra'
    elif thumb_index_dist > 0.1 and index_middle_dist > 0.1 and middle_ring_dist > 0.1 and ring_pinky_dist > 0.1:
        return 'papel'
    elif thumb_index_dist > 0.1 and index_middle_dist < 0.1 and middle_ring_dist < 0.1 and ring_pinky_dist > 0.1:
        return 'tijera'
    else:
        return 'desconocido'
