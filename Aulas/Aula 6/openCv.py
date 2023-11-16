import cv2
import numpy as np

def convolucao_opencv(imagem, kernel):
    return cv2.filter2D(imagem, -1, kernel)

# Definindo os kernels
media = np.ones((3, 3)) / 9
gaussiano = cv2.getGaussianKernel(5, 1) * cv2.getGaussianKernel(5, 1).T
laplaciano = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

imagens_info = {
    "lena": {
        "path": "lena.jpg",
        "data": None
    },
    "biel": {
        "path": "biel.png",
        "data": None
    },
    "cameraman": {
        "path": "cameraman.tif",
        "data": None
    }
}

diretorio = "/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 6/image/"

for nome, info in imagens_info.items():
    imagem = cv2.imread(diretorio + info["path"], cv2.IMREAD_GRAYSCALE)
    imagens_info[nome]["data"] = imagem

for nome, info in imagens_info.items():
    imagem = info["data"]

    imagem_media = convolucao_opencv(imagem, media)
    imagem_gauss = convolucao_opencv(imagem, gaussiano)
    imagem_laplac = convolucao_opencv(imagem, laplaciano)
    imagem_sobel_x = convolucao_opencv(imagem, sobel_x)
    imagem_sobel_y = convolucao_opencv(imagem, sobel_y)
    imagem_gradiente = np.sqrt(imagem_sobel_x**2 + imagem_sobel_y**2)
    imagem_laplac_original = imagem + imagem_laplac

    # Visualização com OpenCV
    cv2.imshow('Original', imagem)
    cv2.imshow('Média', imagem_media)
    cv2.imshow('Gaussiano', imagem_gauss)
    cv2.imshow('Laplaciano', imagem_laplac)
    cv2.imshow('Sobel X', imagem_sobel_x)
    cv2.imshow('Sobel Y', imagem_sobel_y)
    cv2.imshow('Gradiente', imagem_gradiente.astype(np.uint8))
    cv2.imshow('Laplac + Original', imagem_laplac_original)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
