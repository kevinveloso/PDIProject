from PIL import Image
import numpy as np

img = Image.open('testpat.1k.png')
pixelMap = img.load()

def keep_in_range(num):
    
    if num > 255:
        num = 255
    elif num < 0:
        num = 0
    
    return num

def mean(img, pixelMap, bias):

    img2 = Image.new(img.mode, img.size)
    newMap = img2.load()

    avg = (1.0/9.0) + bias

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            new_r = 0
            new_g = 0
            new_b = 0

            if i != 0:
                if j != 0:
                    # 0,0
                    new_r += (pixelMap[i-1,j-1][0] * avg)
                    new_g += (pixelMap[i-1,j-1][1] * avg)
                    new_b += (pixelMap[i-1,j-1][2] * avg)
                # 0,1
                new_r += (pixelMap[i-1,j][0] * avg)
                new_g += (pixelMap[i-1,j][1] * avg)
                new_b += (pixelMap[i-1,j][2] * avg)

                if j < (img.size[1] - 1):
                    # 0,2
                    new_r += (pixelMap[i-1,j+1][0] * avg)
                    new_g += (pixelMap[i-1,j+1][1] * avg)
                    new_b += (pixelMap[i-1,j+1][2] * avg)
            
            if j != 0:
                # 1,0
                new_r += (pixelMap[i,j-1][0] * avg)
                new_g += (pixelMap[i,j-1][1] * avg)
                new_b += (pixelMap[i,j-1][2] * avg)

            if j < (img.size[1] - 1):
                # 1,2
                new_r += (pixelMap[i,j+1][0] * avg)
                new_g += (pixelMap[i,j+1][1] * avg)
                new_b += (pixelMap[i,j+1][2] * avg)
              
            if i < (img.size[0] - 1):
                if j != 0:
                    # 2,0
                    new_r += (pixelMap[i+1,j-1][0] * avg)
                    new_g += (pixelMap[i+1,j-1][1] * avg)
                    new_b += (pixelMap[i+1,j-1][2] * avg)
            
                # 2,1
                new_r += (pixelMap[i+1,j][0] * avg)
                new_g += (pixelMap[i+1,j][1] * avg)
                new_b += (pixelMap[i+1,j][2] * avg)
            
                if j < (img.size[1] - 1):
                    # 2,2
                    new_r += (pixelMap[i+1,j+1][0] * avg)
                    new_g += (pixelMap[i+1,j+1][1] * avg)
                    new_b += (pixelMap[i+1,j+1][2] * avg)
            
            # 1,1
            new_r += (pixelMap[i,j][0] * avg)
            new_g += (pixelMap[i,j][1] * avg)
            new_b += (pixelMap[i,j][2] * avg)

            newMap[i,j] = (keep_in_range(int(new_r)), keep_in_range(int(new_g)), keep_in_range(int(new_b)))

    img2.show()

def sobel(img, pixelMap, sobelType, bias):
    img2 = Image.new(img.mode, img.size)
    newMap = img2.load()

    if sobelType == 'V':
        sobelMatrix = [[-1*bias, 0, 1*bias], 
                        [-2*bias, 0, 2*bias],
                        [-1*bias, 0, 1*bias]]
    elif sobelType == 'H':
        sobelMatrix = [[-1*bias, -2*bias, -1*bias], 
                        [0, 0, 0],
                        [1*bias, 2*bias, 1*bias]]

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            new_r = 0
            new_g = 0
            new_b = 0

            if i != 0:
                if j != 0:
                    # 0,0
                    new_r += (pixelMap[i-1,j-1][0] * sobelMatrix[0][0])
                    new_g += (pixelMap[i-1,j-1][1] * sobelMatrix[0][0])
                    new_b += (pixelMap[i-1,j-1][2] * sobelMatrix[0][0])
                # 0,1
                new_r += (pixelMap[i-1,j][0] * sobelMatrix[0][1])
                new_g += (pixelMap[i-1,j][1] * sobelMatrix[0][1])
                new_b += (pixelMap[i-1,j][2] * sobelMatrix[0][1])

                if j < (img.size[1] - 1):
                    # 0,2
                    new_r += (pixelMap[i-1,j+1][0] * sobelMatrix[0][2])
                    new_g += (pixelMap[i-1,j+1][1] * sobelMatrix[0][2])
                    new_b += (pixelMap[i-1,j+1][2] * sobelMatrix[0][2])
            
            if j != 0:
                # 1,0
                new_r += (pixelMap[i,j-1][0] * sobelMatrix[1][0])
                new_g += (pixelMap[i,j-1][1] * sobelMatrix[1][0])
                new_b += (pixelMap[i,j-1][2] * sobelMatrix[1][0])

            if j < (img.size[1] - 1):
                # 1,2
                new_r += (pixelMap[i,j+1][0] * sobelMatrix[1][2])
                new_g += (pixelMap[i,j+1][1] * sobelMatrix[1][2])
                new_b += (pixelMap[i,j+1][2] * sobelMatrix[1][2])
              
            if i < (img.size[0] - 1):
                if j != 0:
                    # 2,0
                    new_r += (pixelMap[i+1,j-1][0] * sobelMatrix[2][0])
                    new_g += (pixelMap[i+1,j-1][1] * sobelMatrix[2][0])
                    new_b += (pixelMap[i+1,j-1][2] * sobelMatrix[2][0])
            
                # 2,1
                new_r += (pixelMap[i+1,j][0] * sobelMatrix[2][1])
                new_g += (pixelMap[i+1,j][1] * sobelMatrix[2][1])
                new_b += (pixelMap[i+1,j][2] * sobelMatrix[2][1])
            
                if j < (img.size[1] - 1):
                    # 2,2
                    new_r += (pixelMap[i+1,j+1][0] * sobelMatrix[2][2])
                    new_g += (pixelMap[i+1,j+1][1] * sobelMatrix[2][2])
                    new_b += (pixelMap[i+1,j+1][2] * sobelMatrix[2][2])
            
            # 1,1
            new_r += (pixelMap[i,j][0] * sobelMatrix[1][1])
            new_g += (pixelMap[i,j][1] * sobelMatrix[1][1])
            new_b += (pixelMap[i,j][2] * sobelMatrix[1][1])

            newMap[i,j] = (keep_in_range(new_r), keep_in_range(new_g), keep_in_range(new_b))

    img2.show()

sobel(img, pixelMap, 'V', 1)