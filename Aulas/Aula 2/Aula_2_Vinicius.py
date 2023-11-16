import numpy as np
import matplotlib.pyplot as plt

colunas = 40
linhas = 20
image_matriz = np.zeros([linhas, colunas])
print(image_matriz.shape)

# Desenhar a letra "V" mais fechado
image_matriz[5, 2] = 255
image_matriz[6, 2] = 255
image_matriz[7, 2] = 255
image_matriz[8, 2] = 255
image_matriz[9, 2] = 255
image_matriz[10, 3] = 255
image_matriz[11, 4] = 255
image_matriz[12, 5] = 255
image_matriz[13, 6] = 255
image_matriz[14, 7] = 255
image_matriz[15, 8] = 255
image_matriz[15, 9] = 255
image_matriz[14, 10] = 255
image_matriz[13, 11] = 255
image_matriz[12, 12] = 255
image_matriz[11, 13] = 255
image_matriz[10, 14] = 255
image_matriz[9, 15] = 255
image_matriz[8, 15] = 255
image_matriz[7, 15] = 255
image_matriz[6, 15] = 255
image_matriz[5, 15] = 255

# Desenhar a letra "S"
image_matriz[5:10, 19] = 255
image_matriz[5, 19:24] = 255
image_matriz[10, 19:23] = 255
image_matriz[10:16, 23] = 255
image_matriz[15, 19:23] = 255

# Desenhar a letra "S"
image_matriz[5:10, 28] = 255
image_matriz[5, 28:33] = 255
image_matriz[10, 28:32] = 255
image_matriz[10:16, 32] = 255
image_matriz[15, 28:33] = 255


# Desenhar o "S"



plt.imshow(image_matriz, cmap='gray')
plt.show()
