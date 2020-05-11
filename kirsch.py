from PIL import Image
import numpy as np

img = Image.open('lighthouse.jpg')
pixelMap = img.load()

def keep_in_range(num):
    
    if num > 255:
        num = 255
    elif num < 0:
        num = 0
    
    return num

def max(values):
    max = values[0]

    for i in range(len(values)):
        if values[i] > max:
            max = values[i]
    return max

def kirsch(img, pixelMap):
    img2 = Image.new(img.mode, img.size)
    newMap = img2.load()

    k_matrix_1 = [[5, 5, 5],
                [-3, 0, -3],
                [-3, -3, -3]]
    k_matrix_2 = [[-3, 5, 5],
                [-3, 0, 5],
                [-3, -3, -3]]
    k_matrix_3 = [[-3, -3, 5],
                [-3, 0, 5],
                [-3, -3, 5]]
    k_matrix_4 = [[-3, -3, -3],
                [-3, 0, 5],
                [-3, 5, 5]]
    k_matrix_5 = [[-3, -3, -3],
                [-3, 0, -3],
                [5, 5, 5]]
    k_matrix_6 = [[-3, -3, -3],
                [5, 0, -3],
                [5, 5, -3]]
    k_matrix_7 = [[5, -3, -3],
                [5, 0, -3],
                [5, -3, -3]]
    k_matrix_8 = [[5, 5, -3],
                [5, 0, -3],
                [-3, -3, -3]]

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            new_r = 0
            new_g = 0
            new_b = 0

            r_values = list()
            g_values = list()
            b_values = list()

            for l in range(1, 8):
                
                if l==1:
                    k_matrix = k_matrix_1
                elif l==2:
                    k_matrix = k_matrix_2
                elif l==3:
                    k_matrix = k_matrix_3
                elif l==4:
                    k_matrix = k_matrix_4
                elif l==5:
                    k_matrix = k_matrix_5
                elif l==6:
                    k_matrix = k_matrix_6
                elif l==7:
                    k_matrix = k_matrix_7
                elif l==8:
                    k_matrix = k_matrix_8

                if i != 0:
                    if j != 0:
                        # 0,0
                        new_r += (pixelMap[i-1,j-1][0] * k_matrix[0][0])
                        new_g += (pixelMap[i-1,j-1][1] * k_matrix[0][0])
                        new_b += (pixelMap[i-1,j-1][2] * k_matrix[0][0])
                    # 0,1
                    new_r += (pixelMap[i-1,j][0] * k_matrix[0][1])
                    new_g += (pixelMap[i-1,j][1] * k_matrix[0][1])
                    new_b += (pixelMap[i-1,j][2] * k_matrix[0][1])

                    if j < (img.size[1] - 1):
                        # 0,2
                        new_r += (pixelMap[i-1,j+1][0] * k_matrix[0][2])
                        new_g += (pixelMap[i-1,j+1][1] * k_matrix[0][2])
                        new_b += (pixelMap[i-1,j+1][2] * k_matrix[0][2])
                
                if j != 0:
                    # 1,0
                    new_r += (pixelMap[i,j-1][0] * k_matrix[1][0])
                    new_g += (pixelMap[i,j-1][1] * k_matrix[1][0])
                    new_b += (pixelMap[i,j-1][2] * k_matrix[1][0])

                if j < (img.size[1] - 1):
                    # 1,2
                    new_r += (pixelMap[i,j+1][0] * k_matrix[1][2])
                    new_g += (pixelMap[i,j+1][1] * k_matrix[1][2])
                    new_b += (pixelMap[i,j+1][2] * k_matrix[1][2])
                
                if i < (img.size[0] - 1):
                    if j != 0:
                        # 2,0
                        new_r += (pixelMap[i+1,j-1][0] * k_matrix[2][0])
                        new_g += (pixelMap[i+1,j-1][1] * k_matrix[2][0])
                        new_b += (pixelMap[i+1,j-1][2] * k_matrix[2][0])
                
                    # 2,1
                    new_r += (pixelMap[i+1,j][0] * k_matrix[2][1])
                    new_g += (pixelMap[i+1,j][1] * k_matrix[2][1])
                    new_b += (pixelMap[i+1,j][2] * k_matrix[2][1])
                
                    if j < (img.size[1] - 1):
                        # 2,2
                        new_r += (pixelMap[i+1,j+1][0] * k_matrix[2][2])
                        new_g += (pixelMap[i+1,j+1][1] * k_matrix[2][2])
                        new_b += (pixelMap[i+1,j+1][2] * k_matrix[2][2])
                
                # 1,1
                new_r += (pixelMap[i,j][0] * k_matrix[1][1])
                new_g += (pixelMap[i,j][1] * k_matrix[1][1])
                new_b += (pixelMap[i,j][2] * k_matrix[1][1])
            
                r_values.append(new_r)
                g_values.append(new_g)
                b_values.append(new_b)

            newMap[i,j] = (keep_in_range(max(r_values)), keep_in_range(max(g_values)), keep_in_range(max(b_values)))

    img2.show()

kirsch(img, pixelMap)