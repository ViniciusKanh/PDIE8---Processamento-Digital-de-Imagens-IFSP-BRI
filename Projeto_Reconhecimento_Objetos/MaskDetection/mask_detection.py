import cv2
import numpy as np
from scipy.spatial import distance
import tensorflow as tf

# Função para detectar rostos em uma imagem
def detect_faces_in_real_time():
    # Carregar o modelo Haar Cascade para detecção de rostos
    face_model = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    if face_model.empty():
        print("Erro: Modelo de classificador Haar Cascade não carregado.")
        return

    # Inicializar a webcam
    cap = cv2.VideoCapture(0)

    # Carregar o modelo de detecção de máscara
    model = tf.keras.models.load_model('saved_model.h5')

    while True:
        # Capturar um frame da webcam
        ret, frame = cap.read()

        if not ret:
            print("Erro ao capturar o frame da webcam.")
            break

        # Converter o frame para escala de cinza
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar rostos no frame em escala de cinza
        faces = face_model.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=4)

        mask_label = {0: 'COM MÁSCARA', 1: 'SEM MÁSCARA'}
        dist_label = {0: (0, 255, 0), 1: (255, 0, 0)}
        MIN_DISTANCE = 50  # Ajuste esse valor conforme necessário

        for i in range(len(faces)):
            (x, y, w, h) = faces[i]
            crop = frame[y:y + h, x:x + w]
            crop = cv2.resize(crop, (128, 128))
            crop = np.reshape(crop, [1, 128, 128, 3]) / 255.0

            # Fazer a previsão do modelo de detecção de máscara
            mask_result = model.predict(crop)

            # Determinar a cor com base no rótulo (com máscara ou sem máscara)
            color = dist_label[0]  # Inicialmente, definimos como verde (com máscara)

            if mask_result.argmax() == 1:  # Se for "SEM MÁSCARA"
                color = dist_label[1]  # Defina a cor como vermelha

            # Desenhar retângulo e rótulo no frame
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 1)
            cv2.putText(frame, mask_label[mask_result.argmax()], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # Exibir o frame com a detecção em tempo real
        cv2.imshow('Detecção de Máscara em Tempo Real', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar a captura da webcam e fechar a janela
    cap.release()
    cv2.destroyAllWindows()

# Iniciar a detecção em tempo real
detect_faces_in_real_time()
