import cv2
import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

def convolucao_scipy(imagem, kernel):
    return convolve2d(imagem, kernel, mode='same', boundary='wrap')

def clamp(imagem, minimo=0, maximo=255):
    return np.clip(imagem, minimo, maximo)

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
    
    if imagem is None:
        print(f"Erro ao ler a imagem {nome}")
        continue

    imagens_info[nome]["data"] = imagem

for nome, info in imagens_info.items():
    if info["data"] is None:
        continue

    imagem = info["data"]

    imagem_media = convolucao_scipy(imagem, media)
    imagem_gauss = convolucao_scipy(imagem, gaussiano)
    imagem_laplac = convolucao_scipy(imagem, laplaciano)
    imagem_sobel_x = convolucao_scipy(imagem, sobel_x)
    imagem_sobel_y = convolucao_scipy(imagem, sobel_y)
    imagem_gradiente = np.sqrt(imagem_sobel_x**2 + imagem_sobel_y**2)
    imagem_laplac_original = clamp(imagem + imagem_laplac)

    fig, axs = plt.subplots(1, 8, figsize=(25, 5))
    axs[0].imshow(imagem, cmap='gray')
    axs[0].set_title('Original')
    axs[0].axis('off')
    axs[1].imshow(imagem_media, cmap='gray')
    axs[1].set_title('Média')
    axs[1].axis('off')
    axs[2].imshow(imagem_gauss, cmap='gray')
    axs[2].set_title('Gaussiano')
    axs[2].axis('off')
    axs[3].imshow(imagem_laplac, cmap='gray')
    axs[3].set_title('Laplaciano')
    axs[3].axis('off')
    axs[4].imshow(imagem_sobel_x, cmap='gray')
    axs[4].set_title('Sobel X')
    axs[4].axis('off')
    axs[5].imshow(imagem_sobel_y, cmap='gray')
    axs[5].set_title('Sobel Y')
    axs[5].axis('off')
    axs[6].imshow(imagem_gradiente, cmap='gray')
    axs[6].set_title('Gradiente')
    axs[6].axis('off')
    axs[7].imshow(imagem_laplac_original, cmap='gray')
    axs[7].set_title('Laplac + Original')
    axs[7].axis('off')

    plt.tight_layout()
    plt.show()
