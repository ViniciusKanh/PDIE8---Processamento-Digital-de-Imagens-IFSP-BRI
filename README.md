# PDIE8 - Processamento Digital de Imagem

![Capa](https://m.media-amazon.com/images/I/71wa841+qgL._AC_UF1000,1000_QL80_.jpg)

##### Repositorio dos Códigos feitos em aula da Disciplina

#### Feito por: Vinicius de Souza Santos
#### Lecionado por: Murilo Varges

## Aula 1 - 31/07 - Apresentação da Disciplina



- Apresentação da disciplina
- Critérios de avaliação
- Introdução ao processamento digital de imagens


Arquivo: [Aula 1 PDF](https://drive.google.com/open?id=1LzKVKFvw2XGuFE5FhlgWHhY7-bYPHXWN&usp=drive_fs)



## Aula 2 - 07/08 - Fundamentos da Imagem Digital


- lementos da percepção visual humana
- Sensores para aquisição de imagens
- Amostragem e quantização
- Exemplos Python 

Arquivo: [Aula 2 - Fundamentos.pdf](https://drive.google.com/open?id=1nsZLlRpdkAYWOO0s6i5_HRwLuNFCCe9c&usp=drive_fs)

Instalaçao de Bibliotecas


```python
!pip install numpy matplotlib pillow opencv-python scipy imageio
```

    Collecting numpy
      Obtaining dependency information for numpy from https://files.pythonhosted.org/packages/7a/72/6d1cbdf0d770016bc9485f9ef02e73d5cb4cf3c726f8e120b860a403d307/numpy-1.26.0-cp312-cp312-macosx_11_0_arm64.whl.metadata
      Downloading numpy-1.26.0-cp312-cp312-macosx_11_0_arm64.whl.metadata (53 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m53.5/53.5 kB[0m [31m2.0 MB/s[0m eta [36m0:00:00[0m
    [?25hCollecting matplotlib
      Obtaining dependency information for matplotlib from https://files.pythonhosted.org/packages/dd/73/8d69b0337a77f73d316232ea67708b4bcfe5a9c54dbc2327b1d1b730a0b6/matplotlib-3.8.0-cp312-cp312-macosx_11_0_arm64.whl.metadata
      Downloading matplotlib-3.8.0-cp312-cp312-macosx_11_0_arm64.whl.metadata (5.8 kB)
    Collecting pillow
      Obtaining dependency information for pillow from https://files.pythonhosted.org/packages/5c/72/6d0a22c3f499e966f8b6b89842dfb915fb9449d0c9aa2b4e336259a7f00c/Pillow-10.0.1-cp312-cp312-macosx_11_0_arm64.whl.metadata
      Downloading Pillow-10.0.1-cp312-cp312-macosx_11_0_arm64.whl.metadata (9.5 kB)
    Collecting opencv-python
      Obtaining dependency information for opencv-python from https://files.pythonhosted.org/packages/a1/f6/57de91ea40c670527cd47a6548bf2cbedc68cec57c041793b256356abad7/opencv_python-4.8.1.78-cp37-abi3-macosx_11_0_arm64.whl.metadata
      Downloading opencv_python-4.8.1.78-cp37-abi3-macosx_11_0_arm64.whl.metadata (19 kB)
    Collecting scipy
      Obtaining dependency information for scipy from https://files.pythonhosted.org/packages/cb/0e/7e2c614d4c892e7fc9f44f4bf16a4661c7f9112f856c3a14f444e43a6ad4/scipy-1.11.3-cp312-cp312-macosx_12_0_arm64.whl.metadata
      Downloading scipy-1.11.3-cp312-cp312-macosx_12_0_arm64.whl.metadata (217 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m217.9/217.9 kB[0m [31m7.8 MB/s[0m eta [36m0:00:00[0m
    [?25hCollecting imageio
      Obtaining dependency information for imageio from https://files.pythonhosted.org/packages/f6/37/e21e6f38b93878ba80302e95b8ccd4718d80f0c53055ccae343e606b1e2d/imageio-2.31.5-py3-none-any.whl.metadata
      Downloading imageio-2.31.5-py3-none-any.whl.metadata (4.6 kB)
    Collecting contourpy>=1.0.1 (from matplotlib)
      Obtaining dependency information for contourpy>=1.0.1 from https://files.pythonhosted.org/packages/32/0b/d7baca3f60d3b3a77c9ba1307c7792befd3c1c775a26c649dca1bfa9b6ba/contourpy-1.1.1-cp312-cp312-macosx_11_0_arm64.whl.metadata
      Downloading contourpy-1.1.1-cp312-cp312-macosx_11_0_arm64.whl.metadata (5.9 kB)
    Collecting cycler>=0.10 (from matplotlib)
      Obtaining dependency information for cycler>=0.10 from https://files.pythonhosted.org/packages/e7/05/c19819d5e3d95294a6f5947fb9b9629efb316b96de511b418c53d245aae6/cycler-0.12.1-py3-none-any.whl.metadata
      Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
    Collecting fonttools>=4.22.0 (from matplotlib)
      Obtaining dependency information for fonttools>=4.22.0 from https://files.pythonhosted.org/packages/67/a3/45ad3ae785f7ec69efe14ee8098f4a6a205d43314288b84075d05f6329e9/fonttools-4.43.1-cp312-cp312-macosx_10_9_universal2.whl.metadata
      Downloading fonttools-4.43.1-cp312-cp312-macosx_10_9_universal2.whl.metadata (152 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m152.4/152.4 kB[0m [31m9.5 MB/s[0m eta [36m0:00:00[0m
    [?25hCollecting kiwisolver>=1.0.1 (from matplotlib)
      Obtaining dependency information for kiwisolver>=1.0.1 from https://files.pythonhosted.org/packages/26/61/58bb691f6880588be3a4801d199bd776032ece07203faf3e4a8b377f7d9b/kiwisolver-1.4.5-cp312-cp312-macosx_11_0_arm64.whl.metadata
      Downloading kiwisolver-1.4.5-cp312-cp312-macosx_11_0_arm64.whl.metadata (6.4 kB)
    Requirement already satisfied: packaging>=20.0 in /Users/viniciussantos/Library/Python/3.12/lib/python/site-packages (from matplotlib) (23.2)
    Collecting pyparsing>=2.3.1 (from matplotlib)
      Obtaining dependency information for pyparsing>=2.3.1 from https://files.pythonhosted.org/packages/39/92/8486ede85fcc088f1b3dba4ce92dd29d126fd96b0008ea213167940a2475/pyparsing-3.1.1-py3-none-any.whl.metadata
      Downloading pyparsing-3.1.1-py3-none-any.whl.metadata (5.1 kB)
    Requirement already satisfied: python-dateutil>=2.7 in /Users/viniciussantos/Library/Python/3.12/lib/python/site-packages (from matplotlib) (2.8.2)
    Requirement already satisfied: six>=1.5 in /Users/viniciussantos/Library/Python/3.12/lib/python/site-packages (from python-dateutil>=2.7->matplotlib) (1.16.0)
    Downloading numpy-1.26.0-cp312-cp312-macosx_11_0_arm64.whl (13.7 MB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m13.7/13.7 MB[0m [31m46.1 MB/s[0m eta [36m0:00:00[0ma [36m0:00:01[0m
    [?25hDownloading matplotlib-3.8.0-cp312-cp312-macosx_11_0_arm64.whl (7.5 MB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m7.5/7.5 MB[0m [31m41.5 MB/s[0m eta [36m0:00:00[0ma [36m0:00:01[0m
    [?25hDownloading Pillow-10.0.1-cp312-cp312-macosx_11_0_arm64.whl (3.3 MB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m3.3/3.3 MB[0m [31m48.9 MB/s[0m eta [36m0:00:00[0ma [36m0:00:01[0m
    [?25hDownloading opencv_python-4.8.1.78-cp37-abi3-macosx_11_0_arm64.whl (33.1 MB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m33.1/33.1 MB[0m [31m18.0 MB/s[0m eta [36m0:00:00[0m00:01[0m00:01[0m
    [?25hDownloading scipy-1.11.3-cp312-cp312-macosx_12_0_arm64.whl (29.6 MB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m29.6/29.6 MB[0m [31m21.4 MB/s[0m eta [36m0:00:00[0m00:01[0m00:01[0m
    [?25hDownloading imageio-2.31.5-py3-none-any.whl (313 kB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m313.2/313.2 kB[0m [31m14.3 MB/s[0m eta [36m0:00:00[0m
    [?25hDownloading contourpy-1.1.1-cp312-cp312-macosx_11_0_arm64.whl (232 kB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m232.7/232.7 kB[0m [31m22.8 MB/s[0m eta [36m0:00:00[0m
    [?25hDownloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
    Downloading fonttools-4.43.1-cp312-cp312-macosx_10_9_universal2.whl (2.7 MB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m2.7/2.7 MB[0m [31m21.7 MB/s[0m eta [36m0:00:00[0m00:01[0m00:01[0m
    [?25hDownloading kiwisolver-1.4.5-cp312-cp312-macosx_11_0_arm64.whl (64 kB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m65.0/65.0 kB[0m [31m10.2 MB/s[0m eta [36m0:00:00[0m
    [?25hDownloading pyparsing-3.1.1-py3-none-any.whl (103 kB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m103.1/103.1 kB[0m [31m15.1 MB/s[0m eta [36m0:00:00[0m
    [?25hInstalling collected packages: pyparsing, pillow, numpy, kiwisolver, fonttools, cycler, scipy, opencv-python, imageio, contourpy, matplotlib
    Successfully installed contourpy-1.1.1 cycler-0.12.1 fonttools-4.43.1 imageio-2.31.5 kiwisolver-1.4.5 matplotlib-3.8.0 numpy-1.26.0 opencv-python-4.8.1.78 pillow-10.0.1 pyparsing-3.1.1 scipy-1.11.3


### Código da Aula

Importando Bibliotecas


```python
import numpy as np
import matplotlib.pyplot as plt

```

Definindo Variaveis e Imprimindo Matriz


```python
colunas = 40
linhas = 20
image_matriz = np.zeros([linhas, colunas])
print(image_matriz.shape)
```

    (20, 40)


Desenhar a letra "V" mais fechado


```python
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
```

Desenhar a letra "S"


```python
image_matriz[5:10, 19] = 255
image_matriz[5, 19:24] = 255
image_matriz[10, 19:23] = 255
image_matriz[10:16, 23] = 255
image_matriz[15, 19:23] = 255
```

Desenhar a letra "S"


```python
image_matriz[5:10, 28] = 255
image_matriz[5, 28:33] = 255
image_matriz[10, 28:32] = 255
image_matriz[10:16, 32] = 255
image_matriz[15, 28:33] = 255

```

Imprimindo Resultado


```python
plt.imshow(image_matriz, cmap='gray')
plt.show()
```


    
![png](output_24_0.png)
    


## Aula 3 - 14/08 - Vizinhança e Operações em imagens

- Relacionamentos básicos entre pixels
- Operações espaciais
  - Transformações geométricas
  - Escala
  - Rotação
  - Translação
  - Cisalhamento
- Transformações de intensidade


Arquivo: [Aula 3 - Operações.pdf](https://drive.google.com/open?id=1nsX7T4KQtU9BfWuyQmspWnh56Uv2t3vg&usp=drive_fs)

### Código da Aula - Exemplo 1

Importando Bibliotecas


```python
import numpy as np
from PIL import Image  
from numpy import asarray
import matplotlib.pyplot as plt
  
```

Lendo a imagem


```python
im = Image.open('/Users/viniciussantos/Library/CloudStorage/GoogleDrive-vinicius.santos@ifsp.edu.br/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 3/imgs/lena_gray_512_salt_pepper.tif')
im.show()
   
im_ndarray = np.array(im)
plt.imshow(im_ndarray,cmap='gray')
plt.show()
```


    
![png](output_32_0.png)
    


Operação Pixel a pixel (escurecer imagem)


```python
im_dark = im_ndarray.copy
im_dark = im_ndarray/4
```

Creat two colums plot


```python
fig = plt.figure()
plt1 = plt.subplot(1,2,1)
plt2 = plt.subplot(1,2,2)
plt1.title.set_text('Original Image')
plt2.title.set_text('Filtered Image')
    
plt2.imshow(im_dark,cmap='gray')
plt1.imshow(im_ndarray, cmap='gray', vmin=0, vmax=500)
plt.show()
```


    
![png](output_36_0.png)
    


### Código da Aula - Exemplo 2

Importando Bibliotecas


```python
import numpy as np
from PIL import Image  
from numpy import asarray
import matplotlib.pyplot as plt  
```

Lendo a imagem


```python
image_pillow = Image.open('/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 3/imgs/lena_gray_512_salt_pepper.tif')
f_image_nd = np.array(image_pillow)
g_image_nd = np.zeros(f_image_nd.shape)
```

Neighborhood Operatio (Operação por vizinhança)


```python
l = f_image_nd.shape[0]
c = f_image_nd.shape[1]
k = 2 # Kernel size
print("Primeira Imagem")
print(f_image_nd[0:5,0:5])
    
for x in range(k, l-k):
    for y in range(k, c-k):
         s_xy = f_image_nd[x-k:x+k+1, y-k:y+k+1]
         g_image_nd[x,y] = np.median(s_xy).astype(int)
```

    Primeira Imagem
    [[162 162 162 161 162]
     [162 162 162 161 162]
     [162 162 162 161 162]
     [162 162 162 161 162]
     [162 162 255 161 162]]


Creat two colums plot


```python
fig = plt.figure()
plt1 = plt.subplot(1,2,1)
plt2 = plt.subplot(1,2,2)
plt1.title.set_text('Original Image')
plt2.title.set_text('Filtered Image')
    
plt1.imshow(f_image_nd,cmap='gray')
plt2.imshow(g_image_nd, cmap='gray', vmin=0, vmax=500)
plt.show()
```


    
![png](output_45_0.png)
    


## Aula 4 - 21/08 - Exercícios


- Resolução de exercícios sobre fundamentos de imagens digitais;
- Operações ponto a ponto;
- Operações por vizinhança;
- Transformações geométricas.

### Alunos: Giovana Menato e Vinicius Santos

### Exercicio 1

#### [OPERAÇÃO PONTO A PONTO]:
- Calcular o negativo das imagens;
- Diminuir pela metade a intensidade dos pixels;
- Incluir 4 quadrados brancos 10 x 10 pixels em cada canto das imagens;
- Incluir 1 quadrado preto 15X15 no centro das imagens

Importando Bibliotecas


```python
import numpy as np
from PIL import Image  
from numpy import asarray
import matplotlib.pyplot as plt
```

Incorporando o negoativo das imagens


```python
 # Open image
imageLena = Image.open('/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/lena.jpg')
imageHouse = Image.open('/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/house.tif')
imageCamera = Image.open('/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/cameraman.tif')

# convert image to numpy array    
npImageLena = np.array(imageLena) 
npImageHouse = np.array(imageHouse) 
npImageCamera = np.array(imageCamera) 
# Create negative image
npImageNegativeLena = np.array(npImageLena) 
npImageNegativeLena = 255 - npImageNegativeLena;
npImageNegativeHouse = np.array(npImageHouse) 
npImageNegativeHouse = 255 - npImageNegativeHouse;
npImageNegativeCamera = np.array(npImageCamera) 
npImageNegativeCamera = 255 - npImageNegativeCamera;
# Display images and their negatives using Matplotlib
fig, axs = plt.subplots(3, 2, figsize=(10, 15))

# Display original images
axs[0, 0].imshow(npImageLena, cmap='gray')
axs[0, 0].set_title('Original Lena')
axs[0, 0].axis('off')

axs[1, 0].imshow(npImageHouse, cmap='gray')
axs[1, 0].set_title('Original House')
axs[1, 0].axis('off')

axs[2, 0].imshow(npImageCamera, cmap='gray')
axs[2, 0].set_title('Original Camera')
axs[2, 0].axis('off')

# Display negative images
axs[0, 1].imshow(npImageNegativeLena, cmap='gray')
axs[0, 1].set_title('Negative Lena')
axs[0, 1].axis('off')

axs[1, 1].imshow(npImageNegativeHouse, cmap='gray')
axs[1, 1].set_title('Negative House')
axs[1, 1].axis('off')

axs[2, 1].imshow(npImageNegativeCamera, cmap='gray')
axs[2, 1].set_title('Negative Camera')
axs[2, 1].axis('off')

plt.tight_layout()
plt.show()

```


    
![png](output_53_0.png)
    


### Diminuir pela metade a intensidade dos pixels;


```python
# divide by 2 pixels
npImageLena =  (npImageLena / 2).astype(int);
npImageHouse =  (npImageHouse / 2).astype(int);
npImageCamera =  (npImageCamera / 2).astype(int);

print(npImageLena.shape)
print(npImageHouse.shape)
print(npImageCamera.shape)

```

    (300, 300)
    (600, 600)
    (512, 512)


### Incluir 4 quadrados brancos 10 x 10 pixels em cada canto das imagens



```python
imageLena = Image.open('/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/lena.jpg')
imageHouse = Image.open('/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/house.tif')
imageCamera = Image.open('/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/cameraman.tif')

# convert image to numpy array    
npImageLena = np.array(imageLena) 
npImageHouse = np.array(imageHouse) 
npImageCamera = np.array(imageCamera) 
# Add white squares to the corners of the Camera image
npImageCamera[0:11,0:11] = 255
npImageCamera[501:512, 501:512] = 255
npImageCamera[0:11, 501:512] = 255
npImageCamera[501:512, 0:11] = 255

# Add white squares to the corners of the Lena image
npImageLena[0:11,0:11] = 255
npImageLena[589:600, 589:600] = 255
npImageLena[0:11, 589:600] = 255
npImageLena[589:600, 0:11] = 255

# Add white squares to the corners of the House image
npImageHouse[0:11,0:11] = 255
npImageHouse[589:600, 589:600] = 255
npImageHouse[0:11, 589:600] = 255
npImageHouse[589:600, 0:11] = 255

# Display the images using Matplotlib
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Display Camera image with white squares
axs[0].imshow(npImageCamera, cmap='gray')
axs[0].set_title('Camera with Squares')
axs[0].axis('off')

# Display Lena image with white squares
axs[1].imshow(npImageLena, cmap='gray')
axs[1].set_title('Lena with Squares')
axs[1].axis('off')

# Display House image with white squares
axs[2].imshow(npImageHouse, cmap='gray')
axs[2].set_title('House with Squares')
axs[2].axis('off')

plt.tight_layout()
plt.show()


```


    
![png](output_57_0.png)
    


### Incluir 1 quadrado preto 15X15 no centro das imagens


```python
imageLena = Image.open('/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/lena.jpg')
imageHouse = Image.open('/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/house.tif')
imageCamera = Image.open('/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/cameraman.tif')

# convert image to numpy array    
npImageLena = np.array(imageLena) 
npImageHouse = np.array(imageHouse) 
npImageCamera = np.array(imageCamera) 

npImageLena =  (npImageLena / 2).astype(int);
npImageHouse =  (npImageHouse / 2).astype(int);
npImageCamera =  (npImageCamera / 2).astype(int);

npImageLena[142:157,142:157] = 0
npImageCamera[248:263,248:263] = 0
npImageHouse[292:307,292:307] = 0

# Display the images using Matplotlib
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Display Camera image with white squares
axs[0].imshow(npImageCamera, cmap='gray')
axs[0].set_title('Camera with Squares black')
axs[0].axis('off')

# Display Lena image with white squares
axs[1].imshow(npImageLena, cmap='gray')
axs[1].set_title('Lena with Squares black')
axs[1].axis('off')

# Display House image with white squares
axs[2].imshow(npImageHouse, cmap='gray')
axs[2].set_title('House with Squares black')
axs[2].axis('off')

plt.tight_layout()
plt.show()


```


    
![png](output_59_0.png)
    


### Exercicio 2

#### [OPERAÇÃO POR VIZINHANÇA]:
Utilizar kernel 3x3 pixels e desconsiderar pixels das extremidades. Para cada filtro implementar utilizando apenas numpy, utilizando pillow, utilizando opencv e utilizando scipy.

- Calcular o filtro da média;
- Calcular o filtro da mediana;

### Calcular o filtro da média
### Calcular o filtro da mediana


```python
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
```

### Incorporando as Imagens pelo Numpy


```python

# Load images using Pillow
lena_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/lena.jpg'
cam_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/cameraman.tif'
house_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/house.tif'

lena = np.array(Image.open(lena_path).convert('L'))
cam = np.array(Image.open(cam_path).convert('L'))
house = np.array(Image.open(house_path).convert('L'))

def apply_neighborhood_operation_mean(image, k=3):
    output_image = np.zeros(image.shape)
    l, c = image.shape
    for x in range(k, l-k):
        for y in range(k, c-k):
            s_xy = image[x-k:x+k+1, y-k:y+k+1]
            output_image[x, y] = np.mean(s_xy).astype(int)
    return output_image

def apply_neighborhood_operation_median(image, k=3):
    output_image = np.zeros(image.shape)
    l, c = image.shape
    for x in range(k, l-k):
        for y in range(k, c-k):
            s_xy = image[x-k:x+k+1, y-k:y+k+1]
            output_image[x, y] = np.median(s_xy).astype(int)
    return output_image

# Apply neighborhood operation (mean) to each image
g_image_ndLena_mean = apply_neighborhood_operation_mean(lena)
g_image_ndCam_mean = apply_neighborhood_operation_mean(cam)
g_image_ndHouse_mean = apply_neighborhood_operation_mean(house)

# Apply neighborhood operation (median) to each image
g_image_ndLena_median = apply_neighborhood_operation_median(lena)
g_image_ndCam_median = apply_neighborhood_operation_median(cam)
g_image_ndHouse_median = apply_neighborhood_operation_median(house)

# Display images
fig, axs = plt.subplots(3, 3, figsize=(15, 15))

# Display Lena images
axs[0, 0].imshow(lena, cmap='gray')
axs[0, 0].set_title('Original Lena')
axs[0, 1].imshow(g_image_ndLena_mean, cmap='gray')
axs[0, 1].set_title('Lena (Mean Filter)')
axs[0, 2].imshow(g_image_ndLena_median, cmap='gray')
axs[0, 2].set_title('Lena (Median Filter)')

# Display Cameraman images
axs[1, 0].imshow(cam, cmap='gray')
axs[1, 0].set_title('Original Cameraman')
axs[1, 1].imshow(g_image_ndCam_mean, cmap='gray')
axs[1, 1].set_title('Cameraman (Mean Filter)')
axs[1, 2].imshow(g_image_ndCam_median, cmap='gray')
axs[1, 2].set_title('Cameraman (Median Filter)')

# Display House images
axs[2, 0].imshow(house, cmap='gray')
axs[2, 0].set_title('Original House')
axs[2, 1].imshow(g_image_ndHouse_mean, cmap='gray')
axs[2, 1].set_title('House (Mean Filter)')
axs[2, 2].imshow(g_image_ndHouse_median, cmap='gray')
axs[2, 2].set_title('House (Median Filter)')

for ax in axs.ravel():
    ax.axis('off')

plt.tight_layout()
plt.show()
```


    
![png](output_64_0.png)
    


### Incorporando as Imagens pelo Pillow

Importando Bibliotecas


```python
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
```


```python
def apply_neighborhood_operation(img, operation='mean'):
    width, height = img.size
    new_img = Image.new('L', (width, height))
    pixels = img.load()
    new_pixels = new_img.load()

    for x in range(1, width-1):
        for y in range(1, height-1):
            # Extract 3x3 neighborhood
            neighborhood = [
                pixels[x-1, y-1], pixels[x, y-1], pixels[x+1, y-1],
                pixels[x-1, y], pixels[x, y], pixels[x+1, y],
                pixels[x-1, y+1], pixels[x, y+1], pixels[x+1, y+1]
            ]
            
            if operation == 'mean':
                new_pixels[x, y] = sum(neighborhood) // 9
            elif operation == 'median':
                new_pixels[x, y] = sorted(neighborhood)[4]

    return new_img

# Load images
lena_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/lena.jpg'
cam_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/cameraman.tif'
house_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/house.tif'

lena = Image.open(lena_path).convert('L')
cam = Image.open(cam_path).convert('L')
house = Image.open(house_path).convert('L')

# Apply neighborhood operation
lena_mean = apply_neighborhood_operation(lena, 'mean')
cam_mean = apply_neighborhood_operation(cam, 'mean')
house_mean = apply_neighborhood_operation(house, 'mean')

lena_median = apply_neighborhood_operation(lena, 'median')
cam_median = apply_neighborhood_operation(cam, 'median')
house_median = apply_neighborhood_operation(house, 'median')

# Display images
fig, axs = plt.subplots(3, 3, figsize=(15, 15))

# Display Lena images
axs[0, 0].imshow(lena, cmap='gray')
axs[0, 0].set_title('Original Lena')
axs[0, 1].imshow(lena_mean, cmap='gray')
axs[0, 1].set_title('Lena (Mean Filter)')
axs[0, 2].imshow(lena_median, cmap='gray')
axs[0, 2].set_title('Lena (Median Filter)')

# Display Cameraman images
axs[1, 0].imshow(cam, cmap='gray')
axs[1, 0].set_title('Original Cameraman')
axs[1, 1].imshow(cam_mean, cmap='gray')
axs[1, 1].set_title('Cameraman (Mean Filter)')
axs[1, 2].imshow(cam_median, cmap='gray')
axs[1, 2].set_title('Cameraman (Median Filter)')

# Display House images
axs[2, 0].imshow(house, cmap='gray')
axs[2, 0].set_title('Original House')
axs[2, 1].imshow(house_mean, cmap='gray')
axs[2, 1].set_title('House (Mean Filter)')
axs[2, 2].imshow(house_median, cmap='gray')
axs[2, 2].set_title('House (Median Filter)')

for ax in axs.ravel():
    ax.axis('off')

plt.tight_layout()
plt.show()

```


    
![png](output_68_0.png)
    


### Incorporando as Imagens pelo OpenCV

Importando Bibliotecas


```python
import cv2
import matplotlib.pyplot as plt
```


```python


# Load images
lena_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/lena.jpg'
house_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/house.tif'
cam_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/cameraman.tif'

lena = cv2.imread(lena_path, cv2.IMREAD_GRAYSCALE)
house = cv2.imread(house_path, cv2.IMREAD_GRAYSCALE)
cam = cv2.imread(cam_path, cv2.IMREAD_GRAYSCALE)

# Apply mean and median filtering using 3x3 kernel
lena_mean = cv2.blur(lena, (3,3))
lena_median = cv2.medianBlur(lena, 3)

house_mean = cv2.blur(house, (3,3))
house_median = cv2.medianBlur(house, 3)

cam_mean = cv2.blur(cam, (3,3))
cam_median = cv2.medianBlur(cam, 3)

# Display images
fig, axs = plt.subplots(3, 3, figsize=(15, 15))

axs[0, 0].imshow(lena, cmap='gray')
axs[0, 0].set_title('Original Lena')
axs[0, 1].imshow(lena_mean, cmap='gray')
axs[0, 1].set_title('Lena Mean Filtered')
axs[0, 2].imshow(lena_median, cmap='gray')
axs[0, 2].set_title('Lena Median Filtered')

axs[1, 0].imshow(house, cmap='gray')
axs[1, 0].set_title('Original House')
axs[1, 1].imshow(house_mean, cmap='gray')
axs[1, 1].set_title('House Mean Filtered')
axs[1, 2].imshow(house_median, cmap='gray')
axs[1, 2].set_title('House Median Filtered')

axs[2, 0].imshow(cam, cmap='gray')
axs[2, 0].set_title('Original Cameraman')
axs[2, 1].imshow(cam_mean, cmap='gray')
axs[2, 1].set_title('Cameraman Mean Filtered')
axs[2, 2].imshow(cam_median, cmap='gray')
axs[2, 2].set_title('Cameraman Median Filtered')

for ax in axs.ravel():
    ax.axis('off')

plt.tight_layout()
plt.show()
```


    
![png](output_72_0.png)
    


## Utilizando a Biblioteca Scipy

Importando Biblioteca


```python
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage

```


```python
# Load images
lena_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/lena.jpg'
house_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/house.tif'
cam_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/cameraman.tif'

lena = cv2.imread(lena_path, cv2.IMREAD_GRAYSCALE)
house = cv2.imread(house_path, cv2.IMREAD_GRAYSCALE)
cam = cv2.imread(cam_path, cv2.IMREAD_GRAYSCALE)

# Apply mean filtering using 3x3 kernel
kernel = [[1/9, 1/9, 1/9],
          [1/9, 1/9, 1/9],
          [1/9, 1/9, 1/9]]

lena_mean = ndimage.convolve(lena, kernel)
house_mean = ndimage.convolve(house, kernel)
cam_mean = ndimage.convolve(cam, kernel)

# Apply median filtering using 3x3 kernel
lena_median = ndimage.median_filter(lena, size=3)
house_median = ndimage.median_filter(house, size=3)
cam_median = ndimage.median_filter(cam, size=3)

# Display images
fig, axs = plt.subplots(3, 3, figsize=(15, 15))

axs[0, 0].imshow(lena, cmap='gray')
axs[0, 0].set_title('Original Lena')
axs[0, 1].imshow(lena_mean, cmap='gray')
axs[0, 1].set_title('Lena Mean Filtered')
axs[0, 2].imshow(lena_median, cmap='gray')
axs[0, 2].set_title('Lena Median Filtered')

axs[1, 0].imshow(house, cmap='gray')
axs[1, 0].set_title('Original House')
axs[1, 1].imshow(house_mean, cmap='gray')
axs[1, 1].set_title('House Mean Filtered')
axs[1, 2].imshow(house_median, cmap='gray')
axs[1, 2].set_title('House Median Filtered')

axs[2, 0].imshow(cam, cmap='gray')
axs[2, 0].set_title('Original Cameraman')
axs[2, 1].imshow(cam_mean, cmap='gray')
axs[2, 1].set_title('Cameraman Mean Filtered')
axs[2, 2].imshow(cam_median, cmap='gray')
axs[2, 2].set_title('Cameraman Median Filtered')

for ax in axs.ravel():
    ax.axis('off')

plt.tight_layout()
plt.show()
```


    
![png](output_76_0.png)
    


### Exercicio 3

#### [TRANSFORMAÇÕES GEOMÉTRICAS]:
 Para cada filtro implementar utilizando apenas numpy, utilizando pillow, utilizando opencv e utilizando scipy.
- Escala: Redução em 1.5x e aumentar em 2.5x;
- Rotação em 45º, 90º e 100º;
- Translação utilizar os parâmetros que quiser nas coordenadas x e y;
- Translação em 35 pixel no eixo X, 45 eixo Y; 

## Utilizando a Biblioteca Numpy

### Escala: Redução em 1.5x e aumentar em 2.5x
### Rotação em 45º, 90º e 100º

Importando as Biliotecas


```python
import numpy as np
from numpy import asarray
from PIL import Image
from scipy import ndimage

```


```python
def apply_transforms(image_path, title):
    # Open image
    image_in = Image.open(image_path)
    
    # Convert image to numpy array    
    image_np = np.array(image_in) 

    # Zoom or Shrink image
    image_np_zoom = ndimage.zoom(image_np, (2.5, 2.5))
        
    # Rotation image 45º
    image_np_rotate  = ndimage.rotate(image_np, -100, cval=128)

    # Shear image
    height, width = image_np.shape
    transform = [[1, 0, 0],
                 [0.5, 1, 0],
                 [0, 0, 1]]
    image_np_shear = ndimage.affine_transform(image_np,
                                         transform,
                                         offset=(0, -height//2, 0),
                                         output_shape=(height, width+height//2))
    
    # Display images using matplotlib
    fig, axs = plt.subplots(1, 4, figsize=(20, 5))
    axs[0].imshow(image_np, cmap='gray')
    axs[0].set_title(f'Original {title}')
    axs[1].imshow(image_np_zoom, cmap='gray')
    axs[1].set_title(f'Zoomed {title}')
    axs[2].imshow(image_np_rotate, cmap='gray')
    axs[2].set_title(f'Rotated {title}')
    axs[3].imshow(image_np_shear, cmap='gray')
    axs[3].set_title(f'Sheared {title}')
    
    for ax in axs:
        ax.axis('off')
    plt.tight_layout()
    plt.show()

# Paths to the images
image_pathLena = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/lena.jpg'
image_pathHouse = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/house.tif'
image_pathCamera = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/cameraman.tif'

# Apply transformations to each image
apply_transforms(image_pathLena, 'Lena')
apply_transforms(image_pathHouse, 'House')
apply_transforms(image_pathCamera, 'CameraMan')
```


    
![png](output_82_0.png)
    



    
![png](output_82_1.png)
    



    
![png](output_82_2.png)
    


### Translação utilizar os parâmetros que quiser nas coordenadas x e y

Importando Bibliotecas


```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from PIL import Image
```


```python

# Load the images
lena_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/lena.jpg'
cam_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/cameraman.tif'
house_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/house.tif'

lena = np.array(Image.open(lena_path).convert('L'))  # Convert to grayscale
cam = np.array(Image.open(cam_path).convert('L'))
house = np.array(Image.open(house_path).convert('L'))

# Copy the images
translLena = lena.copy()
translCam = cam.copy()
translHouse = house.copy()

# Define the translation (shift) vector
shift_x = 50  
shift_y = -30
shift_vector = [shift_y, shift_x]

# Apply the translation to each image
translated_image_lena = ndimage.shift(translLena, shift_vector, mode='constant', cval=0)
translated_image_cam = ndimage.shift(translCam , shift_vector, mode='constant', cval=0)
translated_image_house = ndimage.shift(translHouse, shift_vector, mode='constant', cval=0)

# Display the translated images using matplotlib
fig = plt.figure(figsize=(15, 5))
plt1 = plt.subplot(1, 3, 1)
plt2 = plt.subplot(1, 3, 2)
plt3 = plt.subplot(1, 3, 3)
plt1.title.set_text("Lena Translação x=50 y=-30")
plt2.title.set_text("Cameraman Translação x=50 y=-30")
plt3.title.set_text("House Translação x=50 y=-30")
plt.subplots_adjust(wspace=0.5)

plt1.imshow(translated_image_lena, cmap="gray")
plt2.imshow(translated_image_cam, cmap="gray")
plt3.imshow(translated_image_house, cmap="gray")

plt.show()
```


    
![png](output_86_0.png)
    


### Translação em 35 pixel no eixo X, 45 eixo Y


```python
# Load the images
lena_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/lena.jpg'
cam_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/cameraman.tif'
house_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/house.tif'

lena = np.array(Image.open(lena_path).convert('L'))  # Convert to grayscale
cam = np.array(Image.open(cam_path).convert('L'))
house = np.array(Image.open(house_path).convert('L'))

# Copy the images
translLena = lena.copy()
translCam = cam.copy()
translHouse = house.copy()

# Define the translation (shift) vector
shift_x = 35  
shift_y = 45
shift_vector = [shift_y, shift_x]

# Apply the translation to each image
translated_image_lena = ndimage.shift(translLena, shift_vector, mode='constant', cval=0)
translated_image_cam = ndimage.shift(translCam , shift_vector, mode='constant', cval=0)
translated_image_house = ndimage.shift(translHouse, shift_vector, mode='constant', cval=0)

# Display the translated images using matplotlib
fig = plt.figure(figsize=(15, 5))
plt1 = plt.subplot(1, 3, 1)
plt2 = plt.subplot(1, 3, 2)
plt3 = plt.subplot(1, 3, 3)
plt1.title.set_text("Lena Translação x=35 y=45")
plt2.title.set_text("Cameraman Translação x=35 y=45")
plt3.title.set_text("House Translação x=35 y=45")
plt.subplots_adjust(wspace=0.5)

plt1.imshow(translated_image_lena, cmap="gray")
plt2.imshow(translated_image_cam, cmap="gray")
plt3.imshow(translated_image_house, cmap="gray")

plt.show()

```


    
![png](output_88_0.png)
    


## Utilizando a Biblioteca Pilow

### Escala: Redução em 1.5x e aumentar em 2.5x
### Rotação em 45º, 90º e 100º

Importando Bibliotecas


```python
from PIL import Image, ImageOps, ImageFilter
import matplotlib.pyplot as plt
```


```python
def apply_transforms(image_path, title):
    # Open image
    image_in = Image.open(image_path)
    
    # Zoom or Shrink image
    size = tuple(int(dim * 2.5) for dim in image_in.size)
    image_zoom = image_in.resize(size, Image.ANTIALIAS)
        
    # Rotation image 45º
    image_rotate = image_in.rotate(100, resample=Image.BICUBIC, fillcolor=128)

    # Shear image
    width, height = image_in.size
    m = -0.5  # Shear factor
    shear_matrix = (1, m, -m*height/2, 0, 1, 0)
    image_shear = image_in.transform((width + int(m*height), height), Image.AFFINE, shear_matrix, Image.BICUBIC)
    
    # Display images using matplotlib
    fig, axs = plt.subplots(1, 4, figsize=(20, 5))
    axs[0].imshow(image_in, cmap='gray')
    axs[0].set_title(f'Original {title}')
    axs[1].imshow(image_zoom, cmap='gray')
    axs[1].set_title(f'Zoomed {title}')
    axs[2].imshow(image_rotate, cmap='gray')
    axs[2].set_title(f'Rotated {title}')
    axs[3].imshow(image_shear, cmap='gray')
    axs[3].set_title(f'Sheared {title}')
    
    for ax in axs:
        ax.axis('off')
    plt.tight_layout()
    plt.show()

# Paths to the images
image_pathLena = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/lena.jpg'
image_pathHouse = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/house.tif'
image_pathCamera = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/cameraman.tif'

# Apply transformations to each image
apply_transforms(image_pathLena, 'Lena')
apply_transforms(image_pathHouse, 'House')
apply_transforms(image_pathCamera, 'CameraMan')



```

    C:\Users\vinny\AppData\Local\Temp\ipykernel_11320\1383239210.py:7: DeprecationWarning: ANTIALIAS is deprecated and will be removed in Pillow 10 (2023-07-01). Use LANCZOS or Resampling.LANCZOS instead.
      image_zoom = image_in.resize(size, Image.ANTIALIAS)



    
![png](output_93_1.png)
    



    
![png](output_93_2.png)
    



    
![png](output_93_3.png)
    


### Translação utilizar os parâmetros que quiser nas coordenadas x e y


```python
# Load the images
lena_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/lena.jpg'
cam_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/cameraman.tif'
house_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/house.tif'

lena = Image.open(lena_path).convert('L')  # Convert to grayscale
cam = Image.open(cam_path).convert('L')
house = Image.open(house_path).convert('L')

# Define the translation (shift) vector
shift_x = 50  
shift_y = -30

# Apply the translation to each image
translated_image_lena = lena.transform(lena.size, Image.AFFINE, (1, 0, shift_x, 0, 1, shift_y), fillcolor=0)
translated_image_cam = cam.transform(cam.size, Image.AFFINE, (1, 0, shift_x, 0, 1, shift_y), fillcolor=0)
translated_image_house = house.transform(house.size, Image.AFFINE, (1, 0, shift_x, 0, 1, shift_y), fillcolor=0)

# Display the translated images using matplotlib
fig = plt.figure(figsize=(15, 5))
plt1 = plt.subplot(1, 3, 1)
plt2 = plt.subplot(1, 3, 2)
plt3 = plt.subplot(1, 3, 3)
plt1.title.set_text("Lena Translação x=50 y=-30")
plt2.title.set_text("Cameraman Translação x=50 y=-30")
plt3.title.set_text("House Translação x=50 y=-30")
plt.subplots_adjust(wspace=0.5)

plt1.imshow(translated_image_lena, cmap="gray")
plt2.imshow(translated_image_cam, cmap="gray")
plt3.imshow(translated_image_house, cmap="gray")

plt.show()
```


    
![png](output_95_0.png)
    


### Translação em 35 pixel no eixo X, 45 eixo Y


```python
# Load the images
lena_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/lena.jpg'
cam_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/cameraman.tif'
house_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/house.tif'

lena = Image.open(lena_path).convert('L')  # Convert to grayscale
cam = Image.open(cam_path).convert('L')
house = Image.open(house_path).convert('L')

# Define the translation (shift) vector
shift_x = 35  
shift_y = 45

# Apply the translation to each image
translated_image_lena = lena.transform(lena.size, Image.AFFINE, (1, 0, shift_x, 0, 1, shift_y), fillcolor=0)
translated_image_cam = cam.transform(cam.size, Image.AFFINE, (1, 0, shift_x, 0, 1, shift_y), fillcolor=0)
translated_image_house = house.transform(house.size, Image.AFFINE, (1, 0, shift_x, 0, 1, shift_y), fillcolor=0)

# Display the translated images using matplotlib
fig = plt.figure(figsize=(15, 5))
plt1 = plt.subplot(1, 3, 1)
plt2 = plt.subplot(1, 3, 2)
plt3 = plt.subplot(1, 3, 3)
plt1.title.set_text("Lena Translação x=35 y=45")
plt2.title.set_text("Cameraman Translação x=35 y=45")
plt3.title.set_text("House Translação x=35 y=45")
plt.subplots_adjust(wspace=0.5)

plt1.imshow(translated_image_lena, cmap="gray")
plt2.imshow(translated_image_cam, cmap="gray")
plt3.imshow(translated_image_house, cmap="gray")

plt.show()

```


    
![png](output_97_0.png)
    


## Utilizando a Biblioteca OpenCV

### Escala: Redução em 1.5x e aumentar em 2.5x
### Rotação em 45º, 90º e 100º

Importando Bliblioteca


```python
import cv2
import matplotlib.pyplot as plt
import numpy as np
```


```python


def apply_transforms(image_path, title):
    # Open image
    image_in = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Zoom or Shrink image
    zoom_scale = 2.5
    image_zoom = cv2.resize(image_in, None, fx=zoom_scale, fy=zoom_scale, interpolation=cv2.INTER_LINEAR)
        
    # Rotation image 45º
    rows, cols = image_in.shape
    M_rotate = cv2.getRotationMatrix2D((cols/2, rows/2), -100, 1)
    image_rotate = cv2.warpAffine(image_in, M_rotate, (cols, rows), borderValue=128)
    
    # Shear image
    M_shear = np.float32([[1, 0.5, -0.5*cols/2], [0, 1, 0]])
    image_shear = cv2.warpAffine(image_in, M_shear, (int(cols + 0.5*rows), rows), borderValue=128)
    
    # Display images using matplotlib
    fig, axs = plt.subplots(1, 4, figsize=(20, 5))
    axs[0].imshow(image_in, cmap='gray')
    axs[0].set_title(f'Original {title}')
    axs[1].imshow(image_zoom, cmap='gray')
    axs[1].set_title(f'Zoomed {title}')
    axs[2].imshow(image_rotate, cmap='gray')
    axs[2].set_title(f'Rotated {title}')
    axs[3].imshow(image_shear, cmap='gray')
    axs[3].set_title(f'Sheared {title}')
    
    for ax in axs:
        ax.axis('off')
    plt.tight_layout()
    plt.show()

# Paths to the images
image_pathLena = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/lena.jpg'
image_pathHouse = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/house.tif'
image_pathCamera = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/cameraman.tif'

# Apply transformations to each image
apply_transforms(image_pathLena, 'Lena')
apply_transforms(image_pathHouse, 'House')
apply_transforms(image_pathCamera, 'CameraMan')

```


    
![png](output_102_0.png)
    



    
![png](output_102_1.png)
    



    
![png](output_102_2.png)
    


### Translação utilizar os parâmetros que quiser nas coordenadas x e y


```python

def apply_translation(image_path, shift_x, shift_y, title):
    # Carregar a imagem
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Definir a matriz de translação
    M = np.float32([[1, 0, shift_x], [0, 1, shift_y]])
    
    # Aplicar a translação
    translated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    
    return translated_image

# Caminhos para as imagens
lena_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/lena.jpg'
cam_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/cameraman.tif'
house_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/house.tif'

# Definir o vetor de translação
shift_x = 50  
shift_y = -30

# Aplicar a translação a cada imagem
translated_image_lena = apply_translation(lena_path, shift_x, shift_y, 'Lena')
translated_image_cam = apply_translation(cam_path, shift_x, shift_y, 'Cameraman')
translated_image_house = apply_translation(house_path, shift_x, shift_y, 'House')

# Exibir as imagens traduzidas usando matplotlib
fig = plt.figure(figsize=(15, 5))
plt1 = plt.subplot(1, 3, 1)
plt2 = plt.subplot(1, 3, 2)
plt3 = plt.subplot(1, 3, 3)
plt1.title.set_text("Lena Translação x=50 y=-30")
plt2.title.set_text("Cameraman Translação x=50 y=-30")
plt3.title.set_text("House Translação x=50 y=-30")
plt.subplots_adjust(wspace=0.5)

plt1.imshow(translated_image_lena, cmap="gray")
plt2.imshow(translated_image_cam, cmap="gray")
plt3.imshow(translated_image_house, cmap="gray")

plt.show()

```


    
![png](output_104_0.png)
    


### Translação em 35 pixel no eixo X, 45 eixo Y


```python

def apply_translation(image_path, shift_x, shift_y):
    # Carregar a imagem
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Definir a matriz de translação
    M = np.float32([[1, 0, shift_x], [0, 1, shift_y]])
    
    # Aplicar a translação
    translated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    
    return translated_image

# Caminhos para as imagens
lena_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/lena.jpg'
cam_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/cameraman.tif'
house_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/house.tif'

# Definir o vetor de translação
shift_x = 35  
shift_y = 45

# Aplicar a translação a cada imagem
translated_image_lena = apply_translation(lena_path, shift_x, shift_y)
translated_image_cam = apply_translation(cam_path, shift_x, shift_y)
translated_image_house = apply_translation(house_path, shift_x, shift_y)

# Exibir as imagens traduzidas usando matplotlib
fig = plt.figure(figsize=(15, 5))
plt1 = plt.subplot(1, 3, 1)
plt2 = plt.subplot(1, 3, 2)
plt3 = plt.subplot(1, 3, 3)
plt1.title.set_text("Lena Translação x=35 y=45")
plt2.title.set_text("Cameraman Translação x=35 y=45")
plt3.title.set_text("House Translação x=35 y=45")
plt.subplots_adjust(wspace=0.5)

plt1.imshow(translated_image_lena, cmap="gray")
plt2.imshow(translated_image_cam, cmap="gray")
plt3.imshow(translated_image_house, cmap="gray")

plt.show()

```


    
![png](output_106_0.png)
    


## Utilizando a Biblioteca Scipy

Importando Biblioteca


```python
import matplotlib.pyplot as plt
from scipy import ndimage
import imageio
```


```python
def apply_transforms(image_path, title):
    # Open image
    image_in = imageio.imread(image_path)
    
    # Convert to grayscale if the image is RGB
    if image_in.ndim == 3:
        image_in = imageio.imread(image_path, as_gray=True)
    
    # Zoom or Shrink image
    image_np_zoom = ndimage.zoom(image_in, 2.5)
        
    # Rotation image 45º
    image_np_rotate  = ndimage.rotate(image_in, -100, cval=128)

    # Shear image
    height, width = image_in.shape
    transform = [[1, 0, 0],
                 [0.5, 1, 0],
                 [0, 0, 1]]
    image_np_shear = ndimage.affine_transform(image_in,
                                         transform,
                                         offset=(0, -height//2),
                                         output_shape=(height, width+height//2))
    
    # Display images using matplotlib
    fig, axs = plt.subplots(1, 4, figsize=(20, 5))
    axs[0].imshow(image_in, cmap='gray')
    axs[0].set_title(f'Original {title}')
    axs[1].imshow(image_np_zoom, cmap='gray')
    axs[1].set_title(f'Zoomed {title}')
    axs[2].imshow(image_np_rotate, cmap='gray')
    axs[2].set_title(f'Rotated {title}')
    axs[3].imshow(image_np_shear, cmap='gray')
    axs[3].set_title(f'Sheared {title}')
    
    for ax in axs:
        ax.axis('off')
    plt.tight_layout()
    plt.show()

# Paths to the images
image_pathLena = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/lena.jpg'
image_pathHouse = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/house.tif'
image_pathCamera = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/cameraman.tif'

# Apply transformations to each image
apply_transforms(image_pathLena, 'Lena')
apply_transforms(image_pathHouse, 'House')
apply_transforms(image_pathCamera, 'CameraMan')


```

    C:\Users\Vinicius\AppData\Local\Temp\ipykernel_8292\1969412905.py:3: DeprecationWarning: Starting with ImageIO v3 the behavior of this function will switch to that of iio.v3.imread. To keep the current behavior (and make this warning disappear) use `import imageio.v2 as imageio` or call `imageio.v2.imread` directly.
      image_in = imageio.imread(image_path)



    
![png](output_110_1.png)
    



    
![png](output_110_2.png)
    



    
![png](output_110_3.png)
    


### Translação utilizar os parâmetros que quiser nas coordenadas x e y


```python

def apply_translation(image_path, shift_x, shift_y, title):
    # Carregar a imagem
    image = imageio.imread(image_path)
    
    # Aplicar a translação
    translated_image = ndimage.shift(image, (shift_y, shift_x))
    return translated_image

# Definir o vetor de translação
shift_x = 50  
shift_y = -30

# Caminhos para as imagens
lena_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/lena.jpg'
cam_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/cameraman.tif'
house_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/house.tif'

# Aplicar a translação a cada imagem
translated_image_lena = apply_translation(lena_path, shift_x, shift_y, 'Lena')
translated_image_cam = apply_translation(cam_path, shift_x, shift_y, 'Cameraman')
translated_image_house = apply_translation(house_path, shift_x, shift_y, 'House')

# Exibir as imagens traduzidas usando matplotlib
fig = plt.figure(figsize=(15, 5))
plt1 = plt.subplot(1, 3, 1)
plt2 = plt.subplot(1, 3, 2)
plt3 = plt.subplot(1, 3, 3)
plt1.title.set_text("Lena Translação x=50 y=-30")
plt2.title.set_text("Cameraman Translação x=50 y=-30")
plt3.title.set_text("House Translação x=50 y=-30")
plt.subplots_adjust(wspace=0.5)

plt1.imshow(translated_image_lena, cmap="gray")
plt2.imshow(translated_image_cam, cmap="gray")
plt3.imshow(translated_image_house, cmap="gray")

plt.show()

```

    C:\Users\Vinicius\AppData\Local\Temp\ipykernel_8292\309799501.py:3: DeprecationWarning: Starting with ImageIO v3 the behavior of this function will switch to that of iio.v3.imread. To keep the current behavior (and make this warning disappear) use `import imageio.v2 as imageio` or call `imageio.v2.imread` directly.
      image = imageio.imread(image_path)



    
![png](output_112_1.png)
    


### Translação em 35 pixel no eixo X, 45 eixo Y


```python
def apply_translation(image_path, shift_x, shift_y):
    # Carregar a imagem
    image = imageio.imread(image_path)
    
    # Aplicar a translação
    translated_image = ndimage.shift(image, (shift_y, shift_x))
    return translated_image

# Definir o vetor de translação
shift_x = 35  
shift_y = 45

# Caminhos para as imagens
lena_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/lena.jpg'
cam_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/cameraman.tif'
house_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 4/images/house.tif'

# Aplicar a translação a cada imagem
translated_image_lena = apply_translation(lena_path, shift_x, shift_y)
translated_image_cam = apply_translation(cam_path, shift_x, shift_y)
translated_image_house = apply_translation(house_path, shift_x, shift_y)

# Exibir as imagens traduzidas usando matplotlib
fig = plt.figure(figsize=(15, 5))
plt1 = plt.subplot(1, 3, 1)
plt2 = plt.subplot(1, 3, 2)
plt3 = plt.subplot(1, 3, 3)
plt1.title.set_text("Lena Translação x=35 y=45")
plt2.title.set_text("Cameraman Translação x=35 y=45")
plt3.title.set_text("House Translação x=35 y=45")
plt.subplots_adjust(wspace=0.5)

plt1.imshow(translated_image_lena, cmap="gray")
plt2.imshow(translated_image_cam, cmap="gray")
plt3.imshow(translated_image_house, cmap="gray")

plt.show()

```

    C:\Users\Vinicius\AppData\Local\Temp\ipykernel_8292\231646287.py:3: DeprecationWarning: Starting with ImageIO v3 the behavior of this function will switch to that of iio.v3.imread. To keep the current behavior (and make this warning disappear) use `import imageio.v2 as imageio` or call `imageio.v2.imread` directly.
      image = imageio.imread(image_path)



    
![png](output_114_1.png)
    


## Aula 5 - 28/08 - Transformações de Intensidade


- Transformações de intensidade
- Fundamentos
- Histograma
- Equalização de histograma

### Exercícios - Transformações e Histograma

- Utilizar as imagens Fig 3.8 e enhance-me.gif disponíveis no Moodle
- Aplicar a transformação logarítmica, testar vários valores para o parâmetro c "s = c log (1 + r)"
- Aplicar a transformação de potência (gama), testar vários valores para o parâmetro γ e c=1 "s = crγ"
- Implemente a representação de cada plano de bits das imagens
- Implementar a equalização do histograma 
- Elaborar relatório explicando a implementação de cada transformação e qual foi o efeito na imagem.

Importando Bibliotecas


```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
```

Funçoes de Transformação


```python
def log_transform(c, img):
    return c * np.log(1 + img)

def power_transform(c, gamma, img):
    return c * np.power(img, gamma)

def bit_plane(img, bit):
    return (img & (1 << bit)) >> bit
```

 Leitura e Processamento das Imagens


```python
enhance_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 5/image/enhance-me.gif'
Fig0308_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 5/image/Fig0308(a)(fractured_spine).tif'

# Leitura das imagens
enhance_img = np.array(Image.open(enhance_path))
Fig0308_img = np.array(Image.open(Fig0308_path))

# Aplicação das transformações
c_values = [1, 5, 10, 20]
gamma_values = [0.1, 0.5, 1, 2, 5]

for c in c_values:
    # Transformação Logarítmica
    transformed_enhance = log_transform(c, enhance_img)
    transformed_Fig0308 = log_transform(c, Fig0308_img)
    
    # Exibição
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(transformed_enhance, cmap='gray')
    axs[0].set_title(f'Enhance-me (c = {c})')
    axs[1].imshow(transformed_Fig0308, cmap='gray')
    axs[1].set_title(f'Fig0308 (c = {c})')
    plt.show()

for gamma in gamma_values:
    # Transformação de Potência (Gama)
    transformed_enhance = power_transform(1, gamma, enhance_img)
    transformed_Fig0308 = power_transform(1, gamma, Fig0308_img)
    
    # Exibição
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(transformed_enhance, cmap='gray')
    axs[0].set_title(f'Enhance-me (γ = {gamma})')
    axs[1].imshow(transformed_Fig0308, cmap='gray')
    axs[1].set_title(f'Fig0308 (γ = {gamma})')
    plt.show()

# Representação de cada plano de bits
for i in range(8):
    bit_enhance = bit_plane(enhance_img, i)
    bit_Fig0308 = bit_plane(Fig0308_img, i)
    
    # Exibição
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(bit_enhance, cmap='gray')
    axs[0].set_title(f'Enhance-me (Bit Plane {i})')
    axs[1].imshow(bit_Fig0308, cmap='gray')
    axs[1].set_title(f'Fig0308 (Bit Plane {i})')
    plt.show()

# Equalização do histograma
equalized_enhance = cv2.equalizeHist(enhance_img)
equalized_Fig0308 = cv2.equalizeHist(Fig0308_img)

# Exibição
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(equalized_enhance, cmap='gray')
axs[0].set_title('Enhance-me (Equalização)')
axs[1].imshow(equalized_Fig0308, cmap='gray')
axs[1].set_title('Fig0308 (Equalização)')
plt.show()

```

    C:\Users\vinny\AppData\Local\Temp\ipykernel_20780\382409465.py:2: RuntimeWarning: divide by zero encountered in log
      return c * np.log(1 + img)



    
![png](output_124_1.png)
    



    
![png](output_124_2.png)
    



    
![png](output_124_3.png)
    



    
![png](output_124_4.png)
    



    
![png](output_124_5.png)
    



    
![png](output_124_6.png)
    



    
![png](output_124_7.png)
    



    
![png](output_124_8.png)
    



    
![png](output_124_9.png)
    



    
![png](output_124_10.png)
    



    
![png](output_124_11.png)
    



    
![png](output_124_12.png)
    



    
![png](output_124_13.png)
    



    
![png](output_124_14.png)
    



    
![png](output_124_15.png)
    



    
![png](output_124_16.png)
    



    
![png](output_124_17.png)
    



    
![png](output_124_18.png)
    


### Relatório: Análise e Implementação de Transformações em Processamento Digital de Imagem

### 1. Introdução

O processamento digital de imagens (PDI) é uma área que se concentra na manipulação e análise de imagens digitais. Este relatório detalha a aplicação de quatro técnicas de PDI em duas imagens distintas: enhance-me.gif e Fig0308(a)(fractured_spine).tif. As técnicas abordadas são: transformação logarítmica, transformação de potência (gama), representação de plano de bits e equalização de histograma.

### 2. Transformação Logarítmica

2.1 Fundamentação Teórica

A transformação logarítmica visa expandir a escala de valores de pixels escuros e comprimir a de pixels claros. É útil para imagens com grandes variações de brilho.

2.2 Implementação

A transformação é aplicada através da fórmula:

s=c×log(1+r)
onde r é o valor do pixel original e c é uma constante.

2.3 Efeito nas Imagens

Ao variar o valor de c, observa-se uma alteração no contraste das imagens. Valores maiores de c resultam em um contraste mais acentuado, enquanto valores menores suavizam o efeito. Esta transformação é especialmente útil para realçar detalhes em regiões escuras das imagens.

### 3. Transformação de Potência (Gama)

3.1 Fundamentação Teórica

A transformação de potência, ou correção gama, é utilizada para ajustar o brilho global de uma imagem.

3.2 Implementação

A transformação é dada pela fórmula:

s=c×r^y, onde γ é o valor que determina o grau de correção.

3.3 Efeito nas Imagens

Valores de γ<1 clareiam a imagem, tornando-a mais luminosa, enquanto valores de γ>1 escurecem a imagem. Esta transformação é útil para ajustar imagens capturadas sob diferentes condições de iluminação.

### 4. Representação de Cada Plano de Bits

4.1 Fundamentação Teórica

Cada pixel de uma imagem em escala de cinza pode ser representado em termos de seus bits individuais.

4.2 Implementação

A representação de cada plano de bits é obtida isolando-se cada bit do valor do pixel.

4.3 Efeito nas Imagens

O plano de bit mais significativo contém a maior parte da informação visual. Planos de bits inferiores contribuem com detalhes mais sutis e, frequentemente, com ruído. Esta técnica é útil para analisar a contribuição de cada bit para a imagem global.

### 5. Equalização do Histograma

5.1 Fundamentação Teórica

A equalização de histograma redistribui os valores de pixel de uma imagem para produzir um histograma uniforme.

5.2 Implementação

A equalização é realizada através da função cv2.equalizeHist().

5.3 Efeito nas Imagens

A técnica melhora o contraste global das imagens, tornando os detalhes mais visíveis e distribuindo a intensidade dos pixels de forma mais uniforme.

### 6. Conclusão

As técnicas de processamento digital de imagem discutidas neste relatório são essenciais para a manipulação e melhoria de imagens digitais. A aplicação destas técnicas em duas imagens distintas demonstrou sua eficácia e versatilidade. A compreensão teórica, juntamente com a implementação prática, fornece uma base sólida para explorar aplicações mais avançadas no campo do PDI.

# Aula 6 - 04/09 - Filtragem Espacial

- Filtragem Espacial
 - Convolução e correlação
 - Máscaras de filmagem espacial

## Atividades - Filtragem Espacial

- Implementar a operação de convolução.
- Utilizando OPENCV, scipy função convolve e implementação manual.
- Implementar seguintes máscaras:
- - Média
- - Guassiano
- - Laplaciano
- - Sobel X
- - Sobel Y
- - Gradiente (Sobel X + Sobel Y)
- - Laplaciano somado a imagem original
- Utilizar as imagens já disponibilizadas: biel, lena, cameraman, etc.

## Utilizando a OpenCV

Importanto Bibliotecas


```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
```

Função de Convolução usando o OpenCV


```python
def convolucao_opencv(imagem, kernel):
    return cv2.filter2D(imagem, -1, kernel)
```

Definindo os kernels


```python
media = np.ones((3, 3)) / 9
gaussiano = cv2.getGaussianKernel(5, 1) * cv2.getGaussianKernel(5, 1).T
laplaciano = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
```

Carregando o diretorio das Imagens


```python
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
```


```python
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
```


    
![png](output_137_0.png)
    



    
![png](output_137_1.png)
    



    
![png](output_137_2.png)
    


## Utilizando o Scipy


Importando Bibliotecas


```python
import cv2
import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
```

Função De Covolução usando Scipy


```python
def convolucao_scipy(imagem, kernel):
    return convolve2d(imagem, kernel, mode='same', boundary='wrap')
```


```python
for nome, info in imagens_info.items():
    imagem = cv2.imread(diretorio + info["path"], cv2.IMREAD_GRAYSCALE)
    imagens_info[nome]["data"] = imagem

for nome, info in imagens_info.items():
    imagem = info["data"]

    imagem_media = convolucao_scipy(imagem, media)
    imagem_gauss = convolucao_scipy(imagem, gaussiano)
    imagem_laplac = convolucao_scipy(imagem, laplaciano)
    imagem_sobel_x = convolucao_scipy(imagem, sobel_x)
    imagem_sobel_y = convolucao_scipy(imagem, sobel_y)
    imagem_gradiente = np.sqrt(imagem_sobel_x**2 + imagem_sobel_y**2)
    imagem_laplac_original = imagem + imagem_laplac
    
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
```


    
![png](output_143_0.png)
    



    
![png](output_143_1.png)
    



    
![png](output_143_2.png)
    


## Utilizando o Metodo Manual

Importando Biblioteca


```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
```

Função de Convolução Manual


```python
def convolucao_manual(imagem, kernel):
    if len(imagem.shape) == 3:  # Verifica se a imagem é colorida (3 canais)
        altura, largura, canais = imagem.shape
    else:  # Caso contrário, é uma imagem em escala de cinza
        altura, largura = imagem.shape
        canais = 1
        imagem = imagem[:, :, np.newaxis]  # Transforma a imagem em um array 3D para uniformidade no processamento

    k_altura, k_largura = kernel.shape
    padding_altura = k_altura // 2
    padding_largura = k_largura // 2

    imagem_padded = np.pad(imagem, ((padding_altura, padding_altura), (padding_largura, padding_largura), (0, 0)), mode='constant')
    saida = np.zeros_like(imagem)

    for canal in range(canais):
        for y in range(altura):
            for x in range(largura):
                saida[y, x, canal] = np.sum(imagem_padded[y:y + k_altura, x:x + k_largura, canal] * kernel)

    if canais == 1:
        saida = saida[:, :, 0]  # Retorna para a forma 2D se a imagem original estava em escala de cinza

    return saida
```


```python
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
```


    
![png](output_149_0.png)
    



    
![png](output_149_1.png)
    



    
![png](output_149_2.png)
    


# Aula 7 - 11/09 - Domínio da Frequência

* Domínio da frequência
* Transformada de Fourier
* Filtragem no domínio da frequência

   ## Atividades - Transformada de Fourier

   * Implementar a Transformada de Fourier (Utilize a biblioteca de sua preferência)
   * Plotar o espectro e fase.
   * Plotar o espectro 3D (Pesquisar formas de visualização 3D em Python)
      - Utilizar as imagens disponibilizadas na aula (Images_fourier.rar)
      - Criar uma imagem fundo branco e um quadrado simulando a função SINC
   * Plotar Original

## Plotando Espectro e Fase

Importando Bibliotecas


```python
import numpy as np
import matplotlib.pyplot as plt
import cv2
```

Imagem Lena


```python
imgLen = cv2.imread("/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 7/image/lena.png", cv2.IMREAD_GRAYSCALE)
```

Processamento para cada imagem


```python
# Função para calcular a Transformada de Fourier 2D e plotar a imagem original, o espectro e a fase
def calcular_e_plotar_fft(imagem, titulo):
    # Calcule a Transformada de Fourier 2D da imagem
    transformada_fourier = np.fft.fft2(imagem)

    # Calcule o espectro de magnitude
    espectro_magnitude = np.abs(transformada_fourier)

    # Calcule a fase
    fase = np.angle(transformada_fourier)

    # Plote a imagem original, o espectro de magnitude e a fase
    plt.figure(figsize=(18, 4))
    
    plt.subplot(1, 3, 1)
    plt.imshow(imagem, cmap='gray')
    plt.title('Imagem Original')
    
    plt.subplot(1, 3, 2)
    plt.imshow(np.log(1 + espectro_magnitude), cmap='gray')
    plt.title('Espectro de Magnitude')
    plt.colorbar()

    plt.subplot(1, 3, 3)
    plt.imshow(fase, cmap='gray')
    plt.title('Fase')
    plt.colorbar()

    plt.tight_layout()
    plt.show()

# Chamada da função para cada imagem
calcular_e_plotar_fft(imgLen, "imgLen")

```


    
![png](output_157_0.png)
    


Imagem Car


```python
imgCar = cv2.imread("/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 7/image/car.tif", cv2.IMREAD_GRAYSCALE)
```


```python
# Função para calcular a Transformada de Fourier 2D e plotar a imagem original, o espectro e a fase
def calcular_e_plotar_fft(imagem, titulo):
    # Calcule a Transformada de Fourier 2D da imagem
    transformada_fourier = np.fft.fft2(imagem)

    # Calcule o espectro de magnitude
    espectro_magnitude = np.abs(transformada_fourier)

    # Calcule a fase
    fase = np.angle(transformada_fourier)

    # Plote a imagem original, o espectro de magnitude e a fase
    plt.figure(figsize=(18, 4))
    
    plt.subplot(1, 3, 1)
    plt.imshow(imagem, cmap='gray')
    plt.title('Imagem Original')
    
    plt.subplot(1, 3, 2)
    plt.imshow(np.log(1 + espectro_magnitude), cmap='gray')
    plt.title('Espectro de Magnitude')
    plt.colorbar()

    plt.subplot(1, 3, 3)
    plt.imshow(fase, cmap='gray')
    plt.title('Fase')
    plt.colorbar()

    plt.tight_layout()
    plt.show()

# Chamada da função para cada imagem
calcular_e_plotar_fft(imgCar, "imgCar")
```


    
![png](output_160_0.png)
    


Imagem newspaper_shot_woman


```python
imgnewspaper_shot_woman = cv2.imread("/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 7/image/newspaper_shot_woman.tif", cv2.IMREAD_GRAYSCALE)
```


```python
# Função para calcular a Transformada de Fourier 2D e plotar a imagem original, o espectro e a fase
def calcular_e_plotar_fft(imagem, titulo):
    # Calcule a Transformada de Fourier 2D da imagem
    transformada_fourier = np.fft.fft2(imagem)

    # Calcule o espectro de magnitude
    espectro_magnitude = np.abs(transformada_fourier)

    # Calcule a fase
    fase = np.angle(transformada_fourier)

    # Plote a imagem original, o espectro de magnitude e a fase
    plt.figure(figsize=(18, 4))
    
    plt.subplot(1, 3, 1)
    plt.imshow(imagem, cmap='gray')
    plt.title('Imagem Original')
    
    plt.subplot(1, 3, 2)
    plt.imshow(np.log(1 + espectro_magnitude), cmap='gray')
    plt.title('Espectro de Magnitude')
    plt.colorbar()

    plt.subplot(1, 3, 3)
    plt.imshow(fase, cmap='gray')
    plt.title('Fase')
    plt.colorbar()

    plt.tight_layout()
    plt.show()

# Chamada da função para cada imagem
calcular_e_plotar_fft(imgnewspaper_shot_woman, "imgnewspaper_shot_woman")
```


    
![png](output_163_0.png)
    


Imagem periodic_noise


```python
imagperiodic_noise = cv2.imread("/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 7/image/periodic_noise.png", cv2.IMREAD_GRAYSCALE)
```


```python
# Função para calcular a Transformada de Fourier 2D e plotar a imagem original, o espectro e a fase
def calcular_e_plotar_fft(imagem, titulo):
    # Calcule a Transformada de Fourier 2D da imagem
    transformada_fourier = np.fft.fft2(imagem)

    # Calcule o espectro de magnitude
    espectro_magnitude = np.abs(transformada_fourier)

    # Calcule a fase
    fase = np.angle(transformada_fourier)

    # Plote a imagem original, o espectro de magnitude e a fase
    plt.figure(figsize=(18, 4))
    
    plt.subplot(1, 3, 1)
    plt.imshow(imagem, cmap='gray')
    plt.title('Imagem Original')
    
    plt.subplot(1, 3, 2)
    plt.imshow(np.log(1 + espectro_magnitude), cmap='gray')
    plt.title('Espectro de Magnitude')
    plt.colorbar()

    plt.subplot(1, 3, 3)
    plt.imshow(fase, cmap='gray')
    plt.title('Fase')
    plt.colorbar()

    plt.tight_layout()
    plt.show()

# Chamada da função para cada imagem
calcular_e_plotar_fft(imagperiodic_noise, "imagperiodic_noise")
```


    
![png](output_166_0.png)
    


Imagem sinc


```python
imagsinc = cv2.imread("/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 7/image/sinc.tif", cv2.IMREAD_GRAYSCALE)
```


```python
# Função para calcular a Transformada de Fourier 2D e plotar a imagem original, o espectro e a fase
def calcular_e_plotar_fft(imagem, titulo):
    # Calcule a Transformada de Fourier 2D da imagem
    transformada_fourier = np.fft.fft2(imagem)

    # Calcule o espectro de magnitude
    espectro_magnitude = np.abs(transformada_fourier)

    # Calcule a fase
    fase = np.angle(transformada_fourier)

    # Plote a imagem original, o espectro de magnitude e a fase
    plt.figure(figsize=(18, 4))
    
    plt.subplot(1, 3, 1)
    plt.imshow(imagem, cmap='gray')
    plt.title('Imagem Original')
    
    plt.subplot(1, 3, 2)
    plt.imshow(np.log(1 + espectro_magnitude), cmap='gray')
    plt.title('Espectro de Magnitude')
    plt.colorbar()

    plt.subplot(1, 3, 3)
    plt.imshow(fase, cmap='gray')
    plt.title('Fase')
    plt.colorbar()

    plt.tight_layout()
    plt.show()

# Chamada da função para cada imagem
calcular_e_plotar_fft(imagsinc, "imagsinc")

```


    
![png](output_169_0.png)
    


## Plotar o espectro 3D (Pesquisar formas de visualização 3D em Python)
      - Utilizar as imagens disponibilizadas na aula (Images_fourier.rar)
      - Criar uma imagem fundo branco e um quadrado simulando a função SINC

Importando Bibliotecas


```python
import numpy as np
import matplotlib.pyplot as plt
import cv2
from mpl_toolkits.mplot3d import Axes3D
```

Carregando as imagens


```python
imgCar = cv2.imread("/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 7/image/car.tif", cv2.IMREAD_GRAYSCALE)
imgLen = cv2.imread("/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 7/image/Lena.png", cv2.IMREAD_GRAYSCALE)
imgNS = cv2.imread("/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 7/image/newspaper_shot_woman.tif", cv2.IMREAD_GRAYSCALE)
imgPeriodic = cv2.imread("/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 7/image/periodic_noise.png", cv2.IMREAD_GRAYSCALE)
imgSinc = cv2.imread("/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 7/image/sinc.png", cv2.IMREAD_GRAYSCALE)
```

Função para calcular e plotar o espectro 3D


```python
def plotar_espectro_3D(imagem, titulo):
    # Calcule a Transformada de Fourier 2D da imagem
    transformada_fourier = np.fft.fft2(imagem)

    # Calcule o espectro 2D
    espectro_2D = np.fft.fftshift(transformada_fourier)

    # Calcule o espectro de magnitude
    espectro_magnitude = np.abs(espectro_2D)

    # Crie uma grade de coordenadas para o espectro 3D
    x = np.fft.fftshift(np.fft.fftfreq(imagem.shape[1]))
    y = np.fft.fftshift(np.fft.fftfreq(imagem.shape[0]))
    X, Y = np.meshgrid(x, y)

    # Plote o espectro 3D
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title('Espectro 3D - ' + titulo)
    ax.plot_surface(X, Y, np.log(1 + espectro_magnitude), cmap='viridis')

    plt.show()
```

Plotando Imagem Carro


```python
plotar_espectro_3D(imgCar, "imgCar")

```


    
![png](output_178_0.png)
    


### Plotando Imagem Lena


```python
plotar_espectro_3D(imgLen, "imgLen")
```


    
![png](output_180_0.png)
    


### Plotando imagem newspaper_shot_woman


```python
plotar_espectro_3D(imgNS, "imgNS")

```


    
![png](output_182_0.png)
    


### Plotando Imagem periodic_noise


```python
plotar_espectro_3D(imgPeriodic, "imgPeriodic")

```


    
![png](output_184_0.png)
    


### Plotando Imagem Sinc


```python
plotar_espectro_3D(imgSinc,"imgSinc")
```


    
![png](output_186_0.png)
    


## Aula 7.2 - 12/09 - Desafios Introdução PDI



### Atividades - Combining Images

* Objetivo: Implementar códigos que utilizam operações básicas combinando duas imagens.

    * Verificação de defeitos em placas: Basicamente realizando uma operação de subtração entre uma imagem de uma placa sem defeito com uma placa com defeito é possivel encontrar defeitos no processo de fabricação: 

     * https://web.stanford.edu/class/ee368/Handouts/Lectures/Examples/3-Combining-Images/Defect_Detection/

* Detecção de movimento: A partir de um vídeo, ao realizar a subtração do fundo da cena sem nenhuma pessoa é possível detectar movimentos: 

    * https://web.stanford.edu/class/ee368/Handouts/Lectures/Examples/3-Combining-Images/Background_Subtraction/

### Verificação de defeitos em placas: Basicamente realizando uma operação de subtração entre uma imagem de uma placa sem defeito com uma placa com defeito é possivel encontrar defeitos no processo de fabricação:


Importanto Bibliotecas



```python
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

```

Carregando as Imagens


```python
placa_ori = np.array(Image.open(r'\Meu Drive\Faculdade\Aula\2023.2\Processamento Digital de Imagem\Aulas\Aula 8\Image\pcbCropped.png'))
placa_def = np.array(Image.open(r'\Meu Drive\Faculdade\Aula\2023.2\Processamento Digital de Imagem\Aulas\Aula 8\Image\pcbCroppedTranslatedDefected.png'))
```


```python
row = placa_ori.shape[1]
col = placa_ori.shape[0]
xShift = 10
yShift = 10
registImg = np.zeros(placa_ori.shape)
registImg[yShift + 1 : row, xShift + 1 : col] = placa_def[1 : row - yShift, 1 : col - xShift]

fig = plt.figure(figsize=(10, 5))
plt1 = plt.subplot(1, 4, 1)
plt2 = plt.subplot(1, 4, 2)
plt3 = plt.subplot(1, 4, 3)
plt4 = plt.subplot(1, 4, 4)
plt1.title.set_text("Original")
plt2.title.set_text('Defeito')
plt3.title.set_text('Sem translação')
plt4.title.set_text('Com translação')
plt1.imshow(placa_ori, cmap='gray')
plt2.imshow(placa_def, cmap='gray')
plt3.imshow((placa_ori - placa_def), cmap='gray')
plt4.imshow(placa_ori - registImg, cmap='gray')
plt.subplots_adjust(wspace=0.5)


```


    
![png](output_195_0.png)
    



```python
import cv2
imgPcbOrigem = cv2.imread("/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 8/Image/pcb.png", cv2.IMREAD_GRAYSCALE)
imgPcbDefeito = cv2.imread("/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 8/Image/pcbDefected.png", cv2.IMREAD_GRAYSCALE)
```

### Detecção de movimento: A partir de um vídeo, ao realizar a subtração do fundo da cena sem nenhuma pessoa é possível detectar movimentos: 

Importando Bibliotecas


```python
import cv2
import numpy as np
```

Abrir o vídeo


```python
video_capture = cv2.VideoCapture('/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 8/Image/surveillance.mpg')
```

Configurar a gravação do vídeo de saída


```python
frame_width = int(video_capture.get(3))
frame_height = int(video_capture.get(4))
out = cv2.VideoWriter('/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 8/Image/Background_Subtraction.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, (frame_width, frame_height))

```

Parâmetros para a subtração de fundo


```python
alpha = 0.95
theta = 0.1
background = None
```


```python
while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Converter o frame para escala de cinza
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if background is None:
        background = gray_frame.astype(float)
        continue

    # Atualizar o modelo de fundo com suavização exponencial
    background = alpha * background + (1 - alpha) * gray_frame

    # Calcular a diferença entre o frame atual e o fundo
    diff_frame = np.abs(gray_frame - background)
    thresh_frame = (diff_frame > theta * 255).astype(np.uint8)

    # Gravar o frame de saída
    out.write(cv2.cvtColor(thresh_frame * 255, cv2.COLOR_GRAY2BGR))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
video_capture.release()
out.release()
cv2.destroyAllWindows()

```

Liberar recursos


```python
video_capture.release()
out.release()
cv2.destroyAllWindows()
```

## Aula 8 - 18/09 - Filtragem no domínio da frequência

* Propriedades da transformada de Fourier
* Filtragem no domínio da frequência
* Filtros passa-alta, passa baixa e passa  banda.

## Atividade: Filtragem Frequência

1.     Calcule e visualize o espectro de uma imagem 512x512 pixels:

    a)  crie e visualize uma imagem simples – quadrado branco sobre fundo preto;

    b)  calcular e visualizar seu espectro de Fourier (amplitudes);

    c)  calcular e visualizar seu espectro de Fourier (fases);

    d)  obter e visualizar seu espectro de Fourier centralizado;

    e)  Aplique uma rotação de 40º no quadrado e repita os passo b-d;

    f)  Aplique uma translação nos eixos x e y no quadrado e repita os passo b-d;

    g)  Aplique um zoom na imagem e repita os passo b-d;

    h)  Explique o que acontece com a transformada de Fourier quando é aplicado a rotação, translação e zoom.


2.     Crie filtros passa-baixa do tipo ideal, butterworth e gaussiano e aplique-o às imagens disponibilizadas. Visualize o seguinte:

    a)  a imagem inicial;

    b)  a imagem do spectro de fourier;

    c)  a imagem de cada filtro;

    d)  a imagem resultante após aplicação de cada filtro.
 

3.     Crie um filtro passa-alta do tipo ideal, butterworth e gaussiano e aplique-o às imagens disponibilizadas. Visualize os mesmos dados da tarefa anterior:

    a)  a imagem inicial;

    b)  a imagem do spectro de fourier;

    c)  a imagem de cada filtro;

    d)  a imagem resultante após aplicação de cada filtro.


4.     Varie o parâmetro de frequência de corte no filtro passa-baixa criado na tarefa 2. Por exemplo, tome valores de D0 iguais a 0,01, 0,05, 0,5. A imagem inicial é igual à anterior. Visualize as imagens dos filtros e as imagens resultantes. Explique os resultados.

5.     Efetue o mesmo que se pede no item 4, mas use o filtro passa-alta em vez do filtro passa-baixa.

6.      Além dos filtros passa-baixa e passa-alta também existe o filtro passa-banda? Explique seu funcionamento e aplique um filtro passa-banda na imagem.

### 1.     Calcule e visualize o espectro de uma imagem 512x512 pixels:

1.  a)  crie e visualize uma imagem simples – quadrado branco sobre fundo preto;


```python
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Criando uma imagem preta de 512x512
imagem = np.zeros((512, 512), dtype=np.uint8)

# Adicionando um quadrado branco no meio da imagem
cv2.rectangle(imagem, (204, 204), (308, 308), 255, -1)

# Visualizando a imagem
plt.imshow(imagem, cmap='gray')
plt.title("Imagem Original")
plt.show()


```


    
![png](output_213_0.png)
    


1. b)  calcular e visualizar seu espectro de Fourier (amplitudes);


```python
# Calculando a Transformada de Fourier
f = np.fft.fft2(imagem)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

# Visualização
plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Espectro de Fourier - Amplitudes')
plt.show()

```


    
![png](output_215_0.png)
    


1. c)  calcular e visualizar seu espectro de Fourier (fases);


```python
# Calculando as fases
fase_spectrum = np.angle(fshift)

# Visualização
plt.imshow(fase_spectrum, cmap = 'gray')
plt.title('Espectro de Fourier - Fases')
plt.show()

```


    
![png](output_217_0.png)
    


1. d)  obter e visualizar seu espectro de Fourier centralizado;


```python
# Calculando a Transformada de Fourier
f = np.fft.fft2(imagem)
fshift = np.fft.fftshift(f)  # Centralizando o espectro
magnitude_spectrum_centered = 20 * np.log(np.abs(fshift) + 1)  # Adicionamos 1 para evitar log(0)

# Visualização do espectro centralizado
plt.imshow(magnitude_spectrum_centered, cmap='gray')
plt.title('Espectro de Fourier Centralizado')
plt.show()

```


    
![png](output_219_0.png)
    


1. e)  Aplique uma rotação de 40º no quadrado e repita os passo b-d;


```python
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Aplicando rotação de 40º na imagem
rows, cols = imagem.shape
M = cv2.getRotationMatrix2D((cols/2, rows/2), 40, 1)
imagem_rotacionada = cv2.warpAffine(imagem, M, (cols, rows))

# b) Calcular e visualizar o espectro de Fourier (amplitudes) da imagem rotacionada
f_rot = np.fft.fft2(imagem_rotacionada)
fshift_rot = np.fft.fftshift(f_rot)
magnitude_spectrum_rot = 20*np.log(np.abs(f_rot)+1)

# c) Calcular e visualizar o espectro de Fourier (fases) da imagem rotacionada
fase_spectrum_rot = np.angle(fshift_rot)

# Utilizando subplots para exibir as imagens lado a lado
fig, axs = plt.subplots(1, 3, figsize=(15,5))

# Imagem rotacionada
axs[0].imshow(imagem_rotacionada, cmap='gray')
axs[0].set_title('Imagem Rotacionada')
axs[0].axis('off')

# Espectro de Amplitude
axs[1].imshow(magnitude_spectrum_rot, cmap='gray')
axs[1].set_title('Espectro de Fourier - Amplitude')
axs[1].axis('off')

# Espectro de Fase
axs[2].imshow(fase_spectrum_rot, cmap='gray')
axs[2].set_title('Espectro de Fourier - Fase')
axs[2].axis('off')

plt.tight_layout()
plt.show()

```


    
![png](output_221_0.png)
    


1. f)  Aplique uma translação nos eixos x e y no quadrado e repita os passo b-d;


```python
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Criação da imagem original: um quadrado branco em um fundo preto
imagem = np.zeros((512, 512), dtype=np.uint8)
cv2.rectangle(imagem, (154, 154), (358, 358), 255, -1)

# Aplicando translação de 40 pixels nos eixos x e y na imagem original
translacao = np.float32([[1, 0, 40], [0, 1, 40]])
imagem_transladada = cv2.warpAffine(imagem, translacao, (512, 512))

# b) Calculando o espectro de Fourier (amplitudes) da imagem transladada
f_trans = np.fft.fft2(imagem_transladada)
fshift_trans = np.fft.fftshift(f_trans)
magnitude_spectrum_trans = 20*np.log(np.abs(fshift_trans) + 1)  # +1 para evitar log(0)

# c) Calculando o espectro de Fourier (fases) da imagem transladada
fase_spectrum_trans = np.angle(fshift_trans)

# Usando subplots para exibir as imagens lado a lado
fig, axs = plt.subplots(1, 3, figsize=(15,5))

# Imagem transladada
axs[0].imshow(imagem_transladada, cmap='gray')
axs[0].set_title('Imagem Transladada')
axs[0].axis('off')

# Espectro de Amplitude
axs[1].imshow(magnitude_spectrum_trans, cmap='gray')
axs[1].set_title('Espectro de Fourier - Amplitude')
axs[1].axis('off')

# Espectro de Fase
axs[2].imshow(fase_spectrum_trans, cmap='gray')
axs[2].set_title('Espectro de Fourier - Fase')
axs[2].axis('off')

plt.tight_layout()
plt.show()



```


    
![png](output_223_0.png)
    


1. g)  Aplique um zoom na imagem e repita os passo b-d;


```python
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Criação da imagem original: um quadrado branco em um fundo preto
imagem = np.zeros((512, 512), dtype=np.uint8)
cv2.rectangle(imagem, (154, 154), (358, 358), 255, -1)

# Aplicando zoom: reduzindo a imagem em 50% e depois aumentando para o tamanho original
imagem_zoom = cv2.resize(imagem, (512, 512))
imagem_zoom = cv2.resize(imagem_zoom, (1024, 1024))

# b) Calculando o espectro de Fourier (amplitudes) da imagem com zoom
f_zoom = np.fft.fft2(imagem_zoom)
fshift_zoom = np.fft.fftshift(f_zoom)
magnitude_spectrum_zoom = 20*np.log(np.abs(fshift_zoom) + 1)  # +1 para evitar log(0)

# c) Calculando o espectro de Fourier (fases) da imagem com zoom
fase_spectrum_zoom = np.angle(fshift_zoom)

# Usando subplots para exibir as imagens lado a lado
fig, axs = plt.subplots(1, 3, figsize=(15,5))

# Imagem com zoom
axs[0].imshow(imagem_zoom, cmap='gray')
axs[0].set_title('Imagem com Zoom')
axs[0].axis('off')

# Espectro de Amplitude
axs[1].imshow(magnitude_spectrum_zoom, cmap='gray')
axs[1].set_title('Espectro de Fourier - Amplitude')
axs[1].axis('off')

# Espectro de Fase
axs[2].imshow(fase_spectrum_zoom, cmap='gray')
axs[2].set_title('Espectro de Fourier - Fase')
axs[2].axis('off')

plt.tight_layout()
plt.show()

```


    
![png](output_225_0.png)
    


1.  h)  Explique o que acontece com a transformada de Fourier quando é aplicado a rotação, translação e zoom.

* Rotação:
Imagem no domínio espacial: Ao aplicarmos uma rotação na imagem no domínio espacial, estamos basicamente rearranjando os pixels de uma maneira rotacionada.

* **Transformada de Fourier:** No domínio da frequência, a rotação da imagem se manifesta como uma rotação correspondente do seu espectro de Fourier. Portanto, se a imagem for rotacionada por um ângulo θ, seu espectro de Fourier também será rotacionado pelo mesmo ângulo θ.

* Translação:
** Imagem no domínio espacial:**  Uma translação simplesmente move a imagem no domínio espacial sem alterar sua orientação ou forma.

    **Transformada de Fourier:**  No domínio da frequência, uma translação da imagem resulta em uma multiplicação do seu espectro de Fourier por um termo exponencial, que corresponde a um deslocamento de fase. Em termos práticos, enquanto a amplitude do espectro permanece inalterada, a fase é modificada. Esta propriedade é crucial em muitas aplicações de processamento de imagem, especialmente quando estamos interessados em analisar ou manipular características de localização de uma imagem.

* Zoom:
**Imagem no domínio espacial:**  O zoom envolve o redimensionamento da imagem, seja ampliando (zoom in) ou reduzindo (zoom out). Isso implica na reamostragem da imagem, e dependendo do método utilizado, pode envolver interpolação ou decimação dos pixels da imagem.

    **Transformada de Fourier:**  No domínio da frequência, um zoom na imagem é manifestado como uma compressão ou expansão do espectro de Fourier. Quando ampliamos uma imagem (zoom in), o espectro de Fourier é comprimido, e quando reduzimos uma imagem (zoom out), o espectro é expandido. É importante notar que, durante essa expansão ou compressão, o conteúdo de alta frequência da imagem pode ser afetado, o que pode levar a perdas de detalhes no caso de um zoom out extensivo.

    Em resumo, a Transformada de Fourier é uma ferramenta poderosa que nos permite analisar e compreender os componentes de frequência de uma imagem. As manipulações no domínio espacial, como rotação, translação e zoom, têm representações correspondentes no domínio da frequência, e entender essas relações é fundamental para o processamento eficaz de imagens e a análise de seus componentes de frequência.

### 2.     Crie filtros passa-baixa do tipo ideal, butterworth e gaussiano e aplique-o às imagens disponibilizadas. Visualize o seguinte:

Caminho das imagens


```python
sinc_original_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 8/img/sinc_original.png'
sinc_original_menor_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 8/img/sinc_original_menor.tif'
sinc_rot_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 8/img/sinc_rot.png'
sinc_rot2_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 8/img/sinc_rot2.png'
sinc_trans_path = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 8/img/sinc_trans.png'
```

Leitura das imagens


```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Ler as imagens
sinc_original = cv2.imread(sinc_original_path, cv2.IMREAD_GRAYSCALE)
sinc_original_menor = cv2.imread(sinc_original_menor_path, cv2.IMREAD_GRAYSCALE)
sinc_rot = cv2.imread(sinc_rot_path, cv2.IMREAD_GRAYSCALE)
sinc_rot2 = cv2.imread(sinc_rot2_path, cv2.IMREAD_GRAYSCALE)
sinc_trans = cv2.imread(sinc_trans_path, cv2.IMREAD_GRAYSCALE)


```

2.  a)  a imagem inicial;


```python
# Crie uma figura para organizar as imagens e legendas
plt.figure(figsize=(15, 5))

# Imagem Original
plt.subplot(151)
plt.imshow(sinc_original, cmap='gray')
plt.title('a) Imagem Original')
plt.axis('off')

# Imagem Rotacionada (40º)
plt.subplot(152)
plt.imshow(sinc_rot, cmap='gray')
plt.title('e) Imagem Rotacionada (40º)')
plt.axis('off')

# Imagem Rotacionada (20º)
plt.subplot(153)
plt.imshow(sinc_rot2, cmap='gray')
plt.title('e) Imagem Rotacionada (20º)')
plt.axis('off')

# Imagem Transladada
plt.subplot(154)
plt.imshow(sinc_trans, cmap='gray')
plt.title('f) Imagem Transladada')
plt.axis('off')

plt.tight_layout()
plt.show()
```


    
![png](output_234_0.png)
    


2. b)  a imagem do spectro de fourier


```python
def fourier_spectrum(image):
    # Computa a transformada de Fourier 2D
    f = np.fft.fft2(image)
    # Centraliza as frequências baixas
    fshift = np.fft.fftshift(f)
    # Calcula a magnitude e aplica o logaritmo para melhor visualização
    magnitude_spectrum = np.log(np.abs(fshift) + 1)
    return magnitude_spectrum

# Computa o espectro de Fourier para todas as imagens
spectrum_original = fourier_spectrum(sinc_original)
spectrum_rot = fourier_spectrum(sinc_rot)
spectrum_rot2 = fourier_spectrum(sinc_rot2)
spectrum_trans = fourier_spectrum(sinc_trans)

# Organização das subplots em uma única linha com 4 colunas
plt.figure(figsize=(20, 5))  # Define o tamanho da figura para melhor visualização

# Espectro de Fourier da Imagem Original
plt.subplot(141)  
plt.imshow(spectrum_original, cmap='gray')
plt.title('b) Espectro de Fourier Original')
plt.axis('off')

# Espectro de Fourier da Imagem Rotacionada 40º
plt.subplot(142)
plt.imshow(spectrum_rot, cmap='gray')
plt.title('b) Espectro de Fourier Rotacionada (40º)')
plt.axis('off')

# Espectro de Fourier da Imagem Rotacionada 20º
plt.subplot(143)
plt.imshow(spectrum_rot2, cmap='gray')
plt.title('b) Espectro de Fourier Rotacionada (20º)')
plt.axis('off')

# Espectro de Fourier da Imagem Transladada
plt.subplot(144)
plt.imshow(spectrum_trans, cmap='gray')
plt.title('b) Espectro de Fourier Transladada')
plt.axis('off')

# Ajusta o layout e mostra a figura
plt.tight_layout()
plt.show()

```


    
![png](output_236_0.png)
    


2. c)  a imagem de cada filtro


```python
def create_filters(image, cutoff):
    # Filtro passa-baixa Ideal
    ideal_filter = ideal_lowpass_filter(image, cutoff)
    
    # Filtro passa-baixa Butterworth
    butter_filter = butterworth_lowpass_filter(image, cutoff)
    
    # Filtro passa-baixa Gaussiano
    gaussian_filter = gaussian_lowpass_filter(image, cutoff)
    
    return ideal_filter, butter_filter, gaussian_filter

def distance(point1, point2):
    """Retorna a distância euclidiana entre dois pontos."""
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def ideal_lowpass_filter(image, cutoff):
    rows, cols = image.shape
    center = (rows / 2, cols / 2)
    filter = np.zeros((rows, cols))
    
    for x in range(cols):
        for y in range(rows):
            if distance((y, x), center) < cutoff:
                filter[y, x] = 1
    return filter

def butterworth_lowpass_filter(image, cutoff, order=2):
    rows, cols = image.shape
    center = (rows / 2, cols / 2)
    filter = np.zeros((rows, cols))
    
    for x in range(cols):
        for y in range(rows):
            filter[y, x] = 1 / (1 + (distance((y, x), center) / cutoff) ** (2 * order))
    return filter

def gaussian_lowpass_filter(image, cutoff):
    rows, cols = image.shape
    center = (rows / 2, cols / 2)
    filter = np.zeros((rows, cols))
    
    for x in range(cols):
        for y in range(rows):
            filter[y, x] = np.exp(-(distance((y, x), center) ** 2) / (2 * (cutoff ** 2)))
    return filter
cutoff = 30  # Você pode ajustar este valor conforme necessário

def normalize_image(image):
    """Normaliza uma imagem para o intervalo [0, 1]."""
    min_val = np.min(image)
    max_val = np.max(image)
    return (image - min_val) / (max_val - min_val)

cutoff = 100  # Ajuste conforme necessário

images = [sinc_original, sinc_rot, sinc_rot2, sinc_trans]
titles = ['Original', 'Rotacionada (40º)', 'Rotacionada (20º)', 'Transladada']

for idx, image in enumerate(images):
    # Cria os filtros
    ideal_filter, butter_filter, gaussian_filter = create_filters(image, cutoff)
    
    # Normaliza para melhor visualização
    ideal_filter = normalize_image(ideal_filter)
    butter_filter = normalize_image(butter_filter)
    gaussian_filter = normalize_image(gaussian_filter)
    
    # Exibe os filtros
    plt.figure(figsize=(15, 5))
    
    # Filtro Ideal
    plt.subplot(131)
    plt.imshow(ideal_filter, cmap='gray')
    plt.title(f'c) Filtro Ideal - {titles[idx]}')
    plt.axis('off')

    # Filtro Butterworth
    plt.subplot(132)
    plt.imshow(butter_filter, cmap='gray')
    plt.title(f'c) Filtro Butterworth - {titles[idx]}')
    plt.axis('off')

    # Filtro Gaussiano
    plt.subplot(133)
    plt.imshow(gaussian_filter, cmap='gray')
    plt.title(f'c) Filtro Gaussiano - {titles[idx]}')
    plt.axis('off')

    # Ajusta o layout e mostra a figura
    plt.tight_layout()
    plt.show()


```


    
![png](output_238_0.png)
    



    
![png](output_238_1.png)
    



    
![png](output_238_2.png)
    



    
![png](output_238_3.png)
    


2. d)  a imagem resultante após aplicação de cada filtro


```python
def apply_filter(image, filter):
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    fshift = fshift * filter
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    return img_back

# Define um cutoff para os filtros
cutoff = 50

# Cria os filtros
ideal_filter = ideal_lowpass_filter(sinc_original, cutoff)
butter_filter = butterworth_lowpass_filter(sinc_original, cutoff)
gaussian_filter = gaussian_lowpass_filter(sinc_original, cutoff)

# Aplica os filtros
img_ideal = apply_filter(sinc_original, ideal_filter)
img_butter = apply_filter(sinc_original, butter_filter)
img_gaussian = apply_filter(sinc_original, gaussian_filter)

# Visualização
fig, axs = plt.subplots(3, 3, figsize=(15,15))

# Imagens originais
axs[0, 0].imshow(sinc_original, cmap='gray')
axs[0, 0].set_title('Original')
axs[0, 1].imshow(ideal_filter, cmap='gray')
axs[0, 1].set_title('Filtro Ideal')
axs[0, 2].imshow(img_ideal, cmap='gray')
axs[0, 2].set_title('Aplicação do Filtro Ideal')

axs[1, 0].imshow(sinc_original, cmap='gray')
axs[1, 0].set_title('Original')
axs[1, 1].imshow(butter_filter, cmap='gray')
axs[1, 1].set_title('Filtro Butterworth')
axs[1, 2].imshow(img_butter, cmap='gray')
axs[1, 2].set_title('Aplicação do Filtro Butterworth')

axs[2, 0].imshow(sinc_original, cmap='gray')
axs[2, 0].set_title('Original')
axs[2, 1].imshow(gaussian_filter, cmap='gray')
axs[2, 1].set_title('Filtro Gaussiano')
axs[2, 2].imshow(img_gaussian, cmap='gray')
axs[2, 2].set_title('Aplicação do Filtro Gaussiano')

for ax in axs.ravel():
    ax.axis('off')

plt.tight_layout()
plt.show()

```


    
![png](output_240_0.png)
    


### 3.     Crie um filtro passa-alta do tipo ideal, butterworth e gaussiano e aplique-o às imagens disponibilizadas. Visualize os mesmos dados da tarefa anterior:

    a)  a imagem inicial;

    b)  a imagem do spectro de fourier;

    c)  a imagem de cada filtro;

    d)  a imagem resultante após aplicação de cada filtro.

Importando Bibliotecas


```python
import numpy as np
import cv2
import matplotlib.pyplot as plt
```

Funções de filtro passa-alta


```python
def ideal_highpass_filter(image, cutoff):
    return 1 - ideal_lowpass_filter(image, cutoff)

def butterworth_highpass_filter(image, cutoff, order=2):
    return 1 - butterworth_lowpass_filter(image, cutoff, order)

def gaussian_highpass_filter(image, cutoff):
    return 1 - gaussian_lowpass_filter(image, cutoff)

# Função para aplicar o filtro usando transformada de Fourier
def apply_filter(image, filter):
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    fshift = fshift * filter
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    return img_back
```

Criação e visualização dos filtros e resultados


```python
images = [sinc_original, sinc_rot, sinc_rot2, sinc_trans]
titles = ['Original', 'Rotacionada (40º)', 'Rotacionada (20º)', 'Transladada']
```


```python
for idx, image in enumerate(images):
    # Fourier
    spectrum = fourier_spectrum(image)
    
    # Criação dos filtros
    ideal_hp = ideal_highpass_filter(image, cutoff)
    butter_hp = butterworth_highpass_filter(image, cutoff)
    gaussian_hp = gaussian_highpass_filter(image, cutoff)

    # Aplicação dos filtros
    result_ideal = apply_filter(image, ideal_hp)
    result_butter = apply_filter(image, butter_hp)
    result_gaussian = apply_filter(image, gaussian_hp)
    
    # Exibição
    plt.figure(figsize=(20, 10))

    # Imagem original
    plt.subplot(4, 4, 1)
    plt.imshow(image, cmap='gray')
    plt.title(f'a) Imagem {titles[idx]}')
    plt.axis('off')

    # Espectro de Fourier
    plt.subplot(4, 4, 2)
    plt.imshow(spectrum, cmap='gray')
    plt.title('b) Espectro de Fourier')
    plt.axis('off')

    # Filtro passa-alta Ideal
    plt.subplot(4, 4, 3)
    plt.imshow(ideal_hp, cmap='gray')
    plt.title('c) Filtro Ideal Passa-Alta')
    plt.axis('off')
    
    # Resultado filtro Ideal
    plt.subplot(4, 4, 4)
    plt.imshow(result_ideal, cmap='gray')
    plt.title('d) Após Filtro Ideal')
    plt.axis('off')

    # Filtro passa-alta Butterworth
    plt.subplot(4, 4, 7)
    plt.imshow(butter_hp, cmap='gray')
    plt.title('c) Filtro Butterworth Passa-Alta')
    plt.axis('off')
    
    # Resultado filtro Butterworth
    plt.subplot(4, 4, 8)
    plt.imshow(result_butter, cmap='gray')
    plt.title('d) Após Filtro Butterworth')
    plt.axis('off')

    # Filtro passa-alta Gaussiano
    plt.subplot(4, 4, 11)
    plt.imshow(gaussian_hp, cmap='gray')
    plt.title('c) Filtro Gaussiano Passa-Alta')
    plt.axis('off')
    
    # Resultado filtro Gaussiano
    plt.subplot(4, 4, 12)
    plt.imshow(result_gaussian, cmap='gray')
    plt.title('d) Após Filtro Gaussiano')
    plt.axis('off')

    # Ajusta o layout e mostra a figura
    plt.tight_layout()
    plt.show()
```


    
![png](output_248_0.png)
    



    
![png](output_248_1.png)
    



    
![png](output_248_2.png)
    



    
![png](output_248_3.png)
    


### 4.     Varie o parâmetro de frequência de corte no filtro passa-baixa criado na tarefa 2. Por exemplo, tome valores de D0 iguais a 0,01, 0,05, 0,5. A imagem inicial é igual à anterior. Visualize as imagens dos filtros e as imagens resultantes. Explique os resultados.

Utilizaremos os valores propostos:

D0 = 0,01
D0 = 0,05
D0 = 0,5

Iremos:

Aplicar os filtros passa-baixa ideal, Butterworth e Gaussiano em cada imagem para cada valor de f0.
Visualizar as imagens dos filtros e as imagens resultantes.


```python
# Definindo os valores de D0 para variação
cutoffs = [0.01, 0.05, 0.5]

for cutoff in cutoffs:
    for idx, image in enumerate(images):
        # Fourier
        spectrum = fourier_spectrum(image)

        # Criação dos filtros
        ideal_lp = ideal_lowpass_filter(image, cutoff)
        butter_lp = butterworth_lowpass_filter(image, cutoff)
        gaussian_lp = gaussian_lowpass_filter(image, cutoff)

        # Aplicação dos filtros
        result_ideal = apply_filter(image, ideal_lp)
        result_butter = apply_filter(image, butter_lp)
        result_gaussian = apply_filter(image, gaussian_lp)

        # Exibição
        plt.figure(figsize=(20, 10))

        # Imagem original
        plt.subplot(4, 4, 1)
        plt.imshow(image, cmap='gray')
        plt.title(f'a) Imagem {titles[idx]}')
        plt.axis('off')

        # Espectro de Fourier
        plt.subplot(4, 4, 2)
        plt.imshow(spectrum, cmap='gray')
        plt.title('b) Espectro de Fourier')
        plt.axis('off')

        # Filtro passa-baixa Ideal
        plt.subplot(4, 4, 3)
        plt.imshow(ideal_lp, cmap='gray')
        plt.title(f'c) Filtro Ideal Passa-Baixa (D0={cutoff})')
        plt.axis('off')

        # Resultado filtro Ideal
        plt.subplot(4, 4, 4)
        plt.imshow(result_ideal, cmap='gray')
        plt.title('d) Após Filtro Ideal')
        plt.axis('off')

        # Filtro passa-baixa Butterworth
        plt.subplot(4, 4, 7)
        plt.imshow(butter_lp, cmap='gray')
        plt.title(f'c) Filtro Butterworth Passa-Baixa (D0={cutoff})')
        plt.axis('off')

        # Resultado filtro Butterworth
        plt.subplot(4, 4, 8)
        plt.imshow(result_butter, cmap='gray')
        plt.title('d) Após Filtro Butterworth')
        plt.axis('off')

        # Filtro passa-baixa Gaussiano
        plt.subplot(4, 4, 11)
        plt.imshow(gaussian_lp, cmap='gray')
        plt.title(f'c) Filtro Gaussiano Passa-Baixa (D0={cutoff})')
        plt.axis('off')

        # Resultado filtro Gaussiano
        plt.subplot(4, 4, 12)
        plt.imshow(result_gaussian, cmap='gray')
        plt.title('d) Após Filtro Gaussiano')
        plt.axis('off')

        # Ajusta o layout e mostra a figura
        plt.tight_layout()
        plt.show()

```


    
![png](output_251_0.png)
    



    
![png](output_251_1.png)
    



    
![png](output_251_2.png)
    



    
![png](output_251_3.png)
    



    
![png](output_251_4.png)
    



    
![png](output_251_5.png)
    



    
![png](output_251_6.png)
    



    
![png](output_251_7.png)
    



    
![png](output_251_8.png)
    



    
![png](output_251_9.png)
    



    
![png](output_251_10.png)
    



    
![png](output_251_11.png)
    


### Explicação dos resultados:

*       D0 = 0,01: Com uma frequência de corte extremamente baixa, esperamos que apenas as componentes de frequência muito baixa da imagem (quase a componente DC) sejam mantidas. A imagem resultante será, principalmente, uma versão muito suavizada ou "blurred" da imagem original.

*       D0 = 0,05: Com uma frequência de corte um pouco maior, mais componentes de frequência da imagem são mantidas. A imagem resultante ainda será suavizada, mas detalhes mais finos começarão a emergir em comparação com D0 = 0,01.

*       D0 = 0,5: Aqui, estamos mantendo a maioria das componentes de frequência baixa da imagem. A imagem resultante será mais próxima da imagem original do que as anteriores, com menos suavização.

*       À medida que aumentamos D0, os detalhes da imagem começam a aparecer devido à permissão de frequências mais altas. A diferença entre os três filtros (ideal, butterworth e gaussiano) estará na forma como eles atenuam as frequências perto do limite de corte. O filtro ideal tem uma transição abrupta, o filtro butterworth tem uma transição suave (com a ordem controlando a nitidez da transição) e o filtro gaussiano tem uma transição que segue uma distribuição gaussiana.

### 5.     Efetue o mesmo que se pede no item 4, mas use o filtro passa-alta em vez do filtro passa-baixa.


```python
def ideal_highpass_filter(image, cutoff):
    rows, cols = image.shape
    center_x, center_y = rows // 2, cols // 2

    filter = np.ones((rows, cols))

    for i in range(rows):
        for j in range(cols):
            if np.sqrt((i - center_x) ** 2 + (j - center_y) ** 2) <= cutoff:
                filter[i, j] = 0
    return filter

def butterworth_highpass_filter(image, cutoff, order=2):
    rows, cols = image.shape
    center_x, center_y = rows // 2, cols // 2

    filter = np.ones((rows, cols))

    for i in range(rows):
        for j in range(cols):
            distance = np.sqrt((i - center_x) ** 2 + (j - center_y) ** 2)
            filter[i, j] = 1 / (1 + (cutoff / distance) ** (2 * order))

    return filter

def gaussian_highpass_filter(image, cutoff):
    rows, cols = image.shape
    center_x, center_y = rows // 2, cols // 2

    filter = np.ones((rows, cols))

    for i in range(rows):
        for j in range(cols):
            distance = np.sqrt((i - center_x) ** 2 + (j - center_y) ** 2)
            filter[i, j] -= np.exp(-(distance ** 2) / (2 * (cutoff ** 2)))

    return filter

def apply_filter(image, filter):
    # Aqui assumo que você está usando a Transformada de Fourier para aplicar o filtro.
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    fshift = fshift * filter
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    
    # Normalizando a imagem resultante para o intervalo [0, 255]
    img_normalized = np.divide(img_back - np.min(img_back), np.max(img_back) - np.min(img_back)) * 255
    
    return img_normalized


```


```python
cutoffs = [0.01, 0.05, 0.5]

for cutoff in cutoffs:
    for idx, image in enumerate(images):
        # Fourier
        spectrum = fourier_spectrum(image)

        # Criação dos filtros
        ideal_hp = ideal_highpass_filter(image, cutoff)
        butter_hp = butterworth_highpass_filter(image, cutoff)
        gaussian_hp = gaussian_highpass_filter(image, cutoff)

        # Aplicação dos filtros
        result_ideal = apply_filter(image, ideal_hp)
        result_butter = apply_filter(image, butter_hp)
        result_gaussian = apply_filter(image, gaussian_hp)

        # Exibição
        plt.figure(figsize=(20, 10))

        # Imagem original
        plt.subplot(4, 4, 1)
        plt.imshow(image, cmap='gray')
        plt.title(f'a) Imagem {titles[idx]}')
        plt.axis('off')

        # Espectro de Fourier
        plt.subplot(4, 4, 2)
        plt.imshow(spectrum, cmap='gray')
        plt.title('b) Espectro de Fourier')
        plt.axis('off')

        # Filtro passa-alta Ideal
        plt.subplot(4, 4, 3)
        plt.imshow(ideal_hp, cmap='gray')
        plt.title(f'c) Filtro Ideal Passa-Alta (D0={cutoff})')
        plt.axis('off')

        # Resultado filtro Ideal
        plt.subplot(4, 4, 4)
        plt.imshow(result_ideal, cmap='gray')
        plt.title('d) Após Filtro Ideal')
        plt.axis('off')

        # Filtro passa-alta Butterworth
        plt.subplot(4, 4, 7)
        plt.imshow(butter_hp, cmap='gray')
        plt.title(f'c) Filtro Butterworth Passa-Alta (D0={cutoff})')
        plt.axis('off')

        # Resultado filtro Butterworth
        plt.subplot(4, 4, 8)
        plt.imshow(result_butter, cmap='gray')
        plt.title('d) Após Filtro Butterworth')
        plt.axis('off')

        # Filtro passa-alta Gaussiano
        plt.subplot(4, 4, 11)
        plt.imshow(gaussian_hp, cmap='gray')
        plt.title(f'c) Filtro Gaussiano Passa-Alta (D0={cutoff})')
        plt.axis('off')

        # Resultado filtro Gaussiano
        plt.subplot(4, 4, 12)
        plt.imshow(result_gaussian, cmap='gray')
        plt.title('d) Após Filtro Gaussiano')
        plt.axis('off')

        # Ajusta o layout e mostra a figura
        plt.tight_layout()
        plt.show()

```

    C:\Users\vinny\AppData\Local\Temp\ipykernel_19816\1729542887.py:22: RuntimeWarning: divide by zero encountered in double_scalars
      filter[i, j] = 1 / (1 + (cutoff / distance) ** (2 * order))



    
![png](output_255_1.png)
    



    
![png](output_255_2.png)
    



    
![png](output_255_3.png)
    



    
![png](output_255_4.png)
    



    
![png](output_255_5.png)
    



    
![png](output_255_6.png)
    



    
![png](output_255_7.png)
    



    
![png](output_255_8.png)
    



    
![png](output_255_9.png)
    



    
![png](output_255_10.png)
    



    
![png](output_255_11.png)
    



    
![png](output_255_12.png)
    


*    D0 = 0,01: Com uma frequência de corte tão baixa no filtro passa-alta, a maior parte da energia da imagem será mantida, resultando em uma imagem quase idêntica à original.

*    D0 = 0,05: A imagem resultante começará a mostrar mais detalhes de alta frequência, como bordas e texturas. Áreas suaves da imagem serão mais atenuadas.

*    D0 = 0,5: Aqui, grande parte das baixas frequências são eliminadas, deixando principalmente os detalhes de alta frequência, como bordas. A imagem resultante aparecerá com mais contraste nas bordas.

*    Os filtros passa-alta realçam os detalhes de alta frequência da imagem. A diferença entre os três filtros (ideal, butterworth e gaussiano) reside na forma como eles atenuam as frequências próximas ao limite de corte.

### 6.      Além dos filtros passa-baixa e passa-alta também existe o filtro passa-banda? Explique seu funcionamento e aplique um filtro passa-banda na imagem.

### Funcionamento do Filtro Passa-Banda:
O filtro passa-banda é projetado para permitir apenas as frequências que estão dentro de uma certa faixa, rejeitando frequências abaixo e acima dessa faixa. É essencialmente a combinação de um filtro passa-alta e um filtro passa-baixa. Especificamente, um filtro passa-banda pode ser obtido multiplicando um filtro passa-baixa por um filtro passa-alta.

A resposta de um filtro passa-banda H(u, v) para uma frequência de corte inferior Dl e uma frequência de corte superior Dh é definido como:

H(u, v) = H_HP(u, v) * H_LP(u, v)

onde:

H_HP(u, v) é a resposta de um filtro passa-alta com frequência de corte Dl.
H_LP(u, v) é a resposta de um filtro passa-baixa com frequência de corte Dh.

### Aplicação do Filtro Passa-Banda na Imagem:


```python
def ideal_bandpass_filter(image, Dl, Dh):
    """Cria um filtro passa-banda ideal."""
    rows, cols = image.shape
    center_x, center_y = rows // 2, cols // 2
    filter = np.zeros((rows, cols), dtype=np.uint8)

    for x in range(rows):
        for y in range(cols):
            distance = np.sqrt((x - center_x)**2 + (y - center_y)**2)
            if Dl <= distance <= Dh:
                filter[x, y] = 1
                
    return filter

def apply_bandpass_filter(image, Dl, Dh):
    """Aplica o filtro passa-banda na imagem."""
    bandpass_filter = ideal_bandpass_filter(image, Dl, Dh)
    filtered_image = apply_filter(image, bandpass_filter)
    return filtered_image

# Aplicando o filtro
Dl = 10
Dh = 50
filtered_image = apply_bandpass_filter(sinc_original, Dl, Dh)

# Exibindo a imagem resultante
plt.figure(figsize=(10, 5))
plt.imshow(filtered_image, cmap='gray')
plt.title("Imagem após aplicação do filtro passa-banda")
plt.axis('off')
plt.show()

```


    
![png](output_259_0.png)
    


*       Este código cria um filtro passa-banda ideal com uma frequência de corte inferior Dl e uma frequência de corte superior Dh e, em seguida, aplica esse filtro à imagem sinc_original. Você pode ajustar Dl e Dh conforme necessário.

## Aula 10 - 02/10 - Morfologia Matemática

### Morfologia 

* Erosão
* Dilatação
* Abertura
* Fechamento

### Trabalho Morfologia

Caminho das Imagens imagens


```python
paths = [
    '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 10 - Trabalho Morfologia/img/{}.tif'.format(i) 
    for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
]
```

Importando Bibliotecas


```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
```

Lendo as Imagens


```python
# Ler as imagens em escala de cinza
images = [cv2.imread(path, cv2.IMREAD_GRAYSCALE) for path in paths]
```


```python
# Configurando o tamanho da figura
plt.figure(figsize=(15, 8))

# Exibindo as imagens
for idx, img in enumerate(images):
    plt.subplot(2, 4, idx+1)
    plt.imshow(img, cmap='gray')
    plt.title(chr(97 + idx) + ')')
    plt.axis('off')

plt.tight_layout()
plt.show()
```


    
![png](output_269_0.png)
    


### Exercicio

1) Implemente a erosão/dilatação utilizando os seguintes elementos estruturantes e utilize todas as imagens: 


```python
# Definindo os elementos estruturantes
se_disk = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
se_cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
se_line = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 1))  # Linha horizontal

# Iterando sobre cada imagem
for idx, img in enumerate(images):
    plt.figure(figsize=(15, 8))

    # Erosão
    img_eroded_disk = cv2.erode(img, se_disk)
    img_eroded_cross = cv2.erode(img, se_cross)
    img_eroded_line = cv2.erode(img, se_line)

    # Dilatação
    img_dilated_disk = cv2.dilate(img, se_disk)
    img_dilated_cross = cv2.dilate(img, se_cross)
    img_dilated_line = cv2.dilate(img, se_line)

    # Subplot 1: Imagem original
    plt.subplot(3, 4, 1)
    plt.imshow(img, cmap='gray')
    plt.title(chr(97 + idx) + ') Original')
    plt.axis('off')

    # Subplots 2-4: Imagens erodidas
    for i, eroded in enumerate([img_eroded_disk, img_eroded_cross, img_eroded_line]):
        plt.subplot(3, 4, i+2)
        plt.imshow(eroded, cmap='gray')
        plt.title(chr(97 + idx) + f') Eroded ({["disk", "cross", "line"][i]})')
        plt.axis('off')

    # Subplots 5-7: Imagens dilatadas
    for i, dilated in enumerate([img_dilated_disk, img_dilated_cross, img_dilated_line]):
        plt.subplot(3, 4, i+5)
        plt.imshow(dilated, cmap='gray')
        plt.title(chr(97 + idx) + f') Dilated ({["disk", "cross", "line"][i]})')
        plt.axis('off')

    plt.tight_layout()
    plt.show()

```


    
![png](output_272_0.png)
    



    
![png](output_272_1.png)
    



    
![png](output_272_2.png)
    



    
![png](output_272_3.png)
    



    
![png](output_272_4.png)
    



    
![png](output_272_5.png)
    



    
![png](output_272_6.png)
    



    
![png](output_272_7.png)
    


2) Implemente as operações de abertura e fechamento utilizando apenas o primeiro elemento estruturante do exercício acima. Considerando as imagens de b) a e) quais imagens seria mais interessante utilizar a abertura e quais o fechamento para remover os ruídos? 


```python

# Definindo o elemento estruturante
se_disk = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# Iterando sobre cada imagem
for idx, img in enumerate(images):
    plt.figure(figsize=(15, 4))

    # Abertura
    img_open = cv2.morphologyEx(img, cv2.MORPH_OPEN, se_disk)

    # Fechamento
    img_close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, se_disk)

    # Subplot 1: Imagem original
    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title(chr(98 + idx) + ') Original')
    plt.axis('off')

    # Subplot 2: Imagem após abertura
    plt.subplot(1, 3, 2)
    plt.imshow(img_open, cmap='gray')
    plt.title(chr(98 + idx) + ') Abertura')
    plt.axis('off')

    # Subplot 3: Imagem após fechamento
    plt.subplot(1, 3, 3)
    plt.imshow(img_close, cmap='gray')
    plt.title(chr(98 + idx) + ') Fechamento')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

```


    
![png](output_274_0.png)
    



    
![png](output_274_1.png)
    



    
![png](output_274_2.png)
    



    
![png](output_274_3.png)
    



    
![png](output_274_4.png)
    



    
![png](output_274_5.png)
    



    
![png](output_274_6.png)
    



    
![png](output_274_7.png)
    


3) Qual sequência de operações poderia ser realizadas para que a imagem f) ficasse apenas com um retângulo branco ao centro? Implemente essas operações.


```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Ler a imagem f) em escala de cinza
path_f = '/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 10 - Trabalho Morfologia/img/f.tif'
image_f = cv2.imread(path_f, cv2.IMREAD_GRAYSCALE)

# Definindo o elemento estruturante
se_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))

# Erosão seguida de dilatação
img_eroded = cv2.erode(image_f, se_rect)
img_dilated = cv2.dilate(img_eroded, se_rect)

# Exibição das imagens
plt.figure(figsize=(15, 5))

# Subplot 1: Imagem original
plt.subplot(1, 3, 1)
plt.imshow(image_f, cmap='gray')
plt.title('f) Original')
plt.axis('off')

# Subplot 2: Imagem após erosão
plt.subplot(1, 3, 2)
plt.imshow(img_eroded, cmap='gray')
plt.title('Após Erosão')
plt.axis('off')

# Subplot 3: Imagem após dilatação
plt.subplot(1, 3, 3)
plt.imshow(img_dilated, cmap='gray')
plt.title('Após Dilatação')
plt.axis('off')

plt.tight_layout()
plt.show()

```


    
![png](output_276_0.png)
    


4) Qual(is) operações seriam necessárias para melhorar a imagem g)? Implemente essa(s) operação(ões). 


```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregando a imagem g)
img_g = cv2.imread('/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 10 - Trabalho Morfologia/img/h.tif', cv2.IMREAD_GRAYSCALE)

# Elemento estruturante (se_disk)
se_disk = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# Dilatação para melhorar o texto
img_processed = cv2.dilate(img_g, se_disk)

# Exibindo a imagem original e a imagem processada
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_g, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(img_processed, cmap='gray')
plt.title('Imagem Processada')
plt.axis('off')

plt.tight_layout()
plt.show()
```


    
![png](output_278_0.png)
    


5) Quais operações seriam necessárias para extrair apenas a borda da imagem h)? Implemente essas operações. 


```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregando a imagem h)
img_h = cv2.imread('/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 10 - Trabalho Morfologia/img/g.tif', cv2.IMREAD_GRAYSCALE)

# Elemento estruturante (se_disk)
se_disk = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# Erosão para extrair a borda
img_eroded = cv2.erode(img_h, se_disk)

# Subtraindo a imagem erodida da imagem original para obter a borda
img_border = cv2.subtract(img_h, img_eroded)

# Exibindo a imagem original e a borda extraída
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_h, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(img_border, cmap='gray')
plt.title('Borda Extraída')
plt.axis('off')

plt.tight_layout()
plt.show()
```


    
![png](output_280_0.png)
    


# Aula 11 - 16/10 - Segmentação - Parte 1

- Segmentação de imagens
- Introdução
- Detecção de pontos
- Detecção de bordas
- Detecção de retas

# Atividades - Segmentação Parte 1

1. Implementar detector de ponto conforme slide 17.

    1.1. Tirar uma foto de uma imagem com um fundo branco e fazer alguns pontos com caneta preta

2. Implementar limiarização, definir 

3. Implementar detector de bordas Canny.

    3.1. Aplicar o filtro de borramento (gaussiano) e verificar se o borramento melhora a detecção de bordas.

    3.2. Mudar os parametros T1 e T2 e avaliar a qualidade das bordas detectadas.



1. Implementar detector de ponto conforme slide 17.

    1.1. Tirar uma foto de uma imagem com um fundo branco e fazer alguns pontos com caneta preta


```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
image = cv2.imread('/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 11/img/lena.png', 0)  # Substitua 'sua_imagem.jpg' pelo caminho da sua imagem

# Parâmetros do detector de pontos Harris
block_size = 2  # Tamanho da vizinhança considerada para cada ponto
ksize = 3  # Tamanho do kernel Sobel usado para calcular gradientes
k = 0.04  # Parâmetro de sensibilidade

# Aplicar o detector de pontos Harris
harris_corners = cv2.cornerHarris(image, block_size, ksize, k)

# Normalizar os resultados para visualização
harris_corners = cv2.normalize(harris_corners, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

# Definir um limite para destacar os cantos
threshold = 100

# Desenhar círculos nos cantos detectados
image_with_corners = image.copy()
image_with_corners[harris_corners > threshold] = 255

# Exibir a imagem original com os cantos destacados
plt.figure(figsize=(8, 6))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Imagem Original')

plt.subplot(1, 2, 2)
plt.imshow(image_with_corners, cmap='gray')
plt.title('Cantos Detectados')

plt.show()

```


    
![png](output_285_0.png)
    


2. Implementar limiarização, definir 


```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carregar a imagem
image = cv2.imread('/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 11/img/fingerprint.png', 0)  # Certifique-se de substituir 'sua_imagem.jpg' pelo caminho da sua imagem

# Aplicar a limiarização
threshold_value = 128  # Você pode ajustar esse valor de acordo com suas necessidades
_, thresholded_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

# Exibir a imagem original e a imagem limiarizada
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Imagem Original')

plt.subplot(1, 2, 2)
plt.imshow(thresholded_image, cmap='gray')
plt.title('Imagem Limiarizada')

plt.show()

```


    
![png](output_287_0.png)
    


3. Implementar detector de bordas Canny.

    3.1. Aplicar o filtro de borramento (gaussiano) e verificar se o borramento melhora a detecção de bordas.


```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
image = cv2.imread('/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 11/img/fingerprint.png', 0)  # Substitua 'sua_imagem.jpg' pelo caminho da sua imagem

# 2.1. Aplicar filtro de borramento gaussiano
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)  # O segundo argumento é o tamanho do kernel gaussiano

# Aplicar o detector de bordas Canny na imagem original
canny_edges = cv2.Canny(image, 100, 200)  # Você pode ajustar os limiares conforme necessário

# Aplicar o detector de bordas Canny na imagem borradad
canny_edges_blurred = cv2.Canny(blurred_image, 100, 200)  # Novamente, ajuste os limiares conforme necessário

# Exibir as imagens
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Imagem Original')

plt.subplot(2, 2, 2)
plt.imshow(blurred_image, cmap='gray')
plt.title('Imagem Borradad (Gaussiano)')

plt.subplot(2, 2, 3)
plt.imshow(canny_edges, cmap='gray')
plt.title('Detecção de Bordas (Canny) na Imagem Original')

plt.subplot(2, 2, 4)
plt.imshow(canny_edges_blurred, cmap='gray')
plt.title('Detecção de Bordas (Canny) na Imagem Borradad')

plt.show()

```


    
![png](output_289_0.png)
    


3.2. Mudar os parametros T1 e T2 e avaliar a qualidade das bordas detectadas.


```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
image = cv2.imread('/Meu Drive/Faculdade/Aula/2023.2/Processamento Digital de Imagem/Aulas/Aula 11/img/fingerprint.png', 0)  # Substitua 'sua_imagem.jpg' pelo caminho da sua imagem

# 2.1. Aplicar filtro de borramento gaussiano
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)  # O segundo argumento é o tamanho do kernel gaussiano

# Definir diferentes valores de T1 e T2
T1_values = [50, 100, 150]
T2_values = [100, 150, 200]

plt.figure(figsize=(12, 12))
plt.suptitle('Efeito dos parâmetros T1 e T2 na Detecção de Bordas', fontsize=16)

for i, (T1, T2) in enumerate(zip(T1_values, T2_values)):
    # Aplicar o detector de bordas Canny com os valores de T1 e T2
    canny_edges = cv2.Canny(image, T1, T2)

    plt.subplot(3, 3, i + 1)
    plt.imshow(canny_edges, cmap='gray')
    plt.title(f'T1={T1}, T2={T2}')

    plt.subplot(3, 3, i + 4)
    canny_edges_blurred = cv2.Canny(blurred_image, T1, T2)
    plt.imshow(canny_edges_blurred, cmap='gray')
    plt.title(f'T1={T1}, T2={T2} (Borradad)')

plt.show()

```


    
![png](output_291_0.png)
    

