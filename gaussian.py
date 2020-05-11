from PIL import Image
import numpy as np

img = Image.open('Captura de tela de 2019-03-09 07-29-00.png')
pixelMap = img.load()

def keep_in_range(num):
    
    if num > 255:
        num = 255
    elif num < 0:
        num = 0
    
    return num


def gaussian(img, pixelMap):
    img2 = Image.new(img.mode, img.size)
    newMap = img2.load()

    gaussianMatrix = [[0.08, 0.165, 0.08], 
                    [0.165, 0.05, 0.165],
                    [0.08, 0.165, 0.08]]

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            new_r = 0
            new_g = 0
            new_b = 0

            if i != 0:
                if j != 0:
                    # 0,0
                    new_r += (pixelMap[i-1,j-1][0] * gaussianMatrix[0][0])
                    new_g += (pixelMap[i-1,j-1][1] * gaussianMatrix[0][0])
                    new_b += (pixelMap[i-1,j-1][2] * gaussianMatrix[0][0])
                # 0,1
                new_r += (pixelMap[i-1,j][0] * gaussianMatrix[0][1])
                new_g += (pixelMap[i-1,j][1] * gaussianMatrix[0][1])
                new_b += (pixelMap[i-1,j][2] * gaussianMatrix[0][1])

                if j < (img.size[1] - 1):
                    # 0,2
                    new_r += (pixelMap[i-1,j+1][0] * gaussianMatrix[0][2])
                    new_g += (pixelMap[i-1,j+1][1] * gaussianMatrix[0][2])
                    new_b += (pixelMap[i-1,j+1][2] * gaussianMatrix[0][2])
            
            if j != 0:
                # 1,0
                new_r += (pixelMap[i,j-1][0] * gaussianMatrix[1][0])
                new_g += (pixelMap[i,j-1][1] * gaussianMatrix[1][0])
                new_b += (pixelMap[i,j-1][2] * gaussianMatrix[1][0])

            if j < (img.size[1] - 1):
                # 1,2
                new_r += (pixelMap[i,j+1][0] * gaussianMatrix[1][2])
                new_g += (pixelMap[i,j+1][1] * gaussianMatrix[1][2])
                new_b += (pixelMap[i,j+1][2] * gaussianMatrix[1][2])
              
            if i < (img.size[0] - 1):
                if j != 0:
                    # 2,0
                    new_r += (pixelMap[i+1,j-1][0] * gaussianMatrix[2][0])
                    new_g += (pixelMap[i+1,j-1][1] * gaussianMatrix[2][0])
                    new_b += (pixelMap[i+1,j-1][2] * gaussianMatrix[2][0])
            
                # 2,1
                new_r += (pixelMap[i+1,j][0] * gaussianMatrix[2][1])
                new_g += (pixelMap[i+1,j][1] * gaussianMatrix[2][1])
                new_b += (pixelMap[i+1,j][2] * gaussianMatrix[2][1])
            
                if j < (img.size[1] - 1):
                    # 2,2
                    new_r += (pixelMap[i+1,j+1][0] * gaussianMatrix[2][2])
                    new_g += (pixelMap[i+1,j+1][1] * gaussianMatrix[2][2])
                    new_b += (pixelMap[i+1,j+1][2] * gaussianMatrix[2][2])
            
            # 1,1
            new_r += (pixelMap[i,j][0] * gaussianMatrix[1][1])
            new_g += (pixelMap[i,j][1] * gaussianMatrix[1][1])
            new_b += (pixelMap[i,j][2] * gaussianMatrix[1][1])

            newMap[i,j] = (keep_in_range(int(new_r)), keep_in_range(int(new_g)), keep_in_range(int(new_b)))

    img2.show()

gaussian(img, pixelMap)