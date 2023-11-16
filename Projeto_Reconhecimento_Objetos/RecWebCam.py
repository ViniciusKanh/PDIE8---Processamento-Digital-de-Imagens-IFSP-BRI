import cv2
import torch

# Carregue o modelo YOLOv5 (pode escolher a versão que preferir)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Inicialize a webcam (0 representa a câmera padrão, ajuste conforme necessário)
cap = cv2.VideoCapture(0)

while True:
    # Capture um frame da webcam
    ret, frame = cap.read()

    # Realize a detecção de objetos no frame
    results = model(frame)

    # Desenhe as detecções no frame
    frame_with_detections = results.render()[0]

    # Mostre o frame com as detecções
    cv2.imshow('Detecção de Objetos', frame_with_detections)

    # Pressione a tecla 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libere os recursos da webcam e feche a janela
cap.release()
cv2.destroyAllWindows()
