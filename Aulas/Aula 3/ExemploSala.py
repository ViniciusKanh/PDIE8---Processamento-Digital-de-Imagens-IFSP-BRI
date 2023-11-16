import numpy as np
from PIL import Image  
from numpy import asarray
import matplotlib.pyplot as plt
  
def main():
    im = Image.open('imgs/lena_gray_512_salt_pepper.tif')
    im.show()
   
    im_ndarray = np.array(im)
    plt.imshow(im_ndarray,cmap='gray')
    plt.show()
    
    #Operação Pixel a pixel (escurecer imagem)
    im_dark = im_ndarray.copy
    im_dark = im_ndarray/4

    # Creat two colums plot
    fig = plt.figure()
    plt1 = plt.subplot(1,2,1)
    plt2 = plt.subplot(1,2,2)
    plt1.title.set_text('Original Image')
    plt2.title.set_text('Filtered Image')
    
    plt2.imshow(im_dark,cmap='gray')
    plt1.imshow(im_ndarray, cmap='gray', vmin=0, vmax=500)
    plt.show()
    
    
if __name__ == "__main__":
    main()