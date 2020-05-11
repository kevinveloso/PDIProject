from PIL import Image
import numpy as np

img = Image.open('108073.png')
pixelMap = img.load()

def median(img, pixelMap):

    img2 = Image.new(img.mode, img.size)
    newMap = img2.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            
            r_values = list()
            g_values = list()
            b_values = list()
            
            if i == 0 or i == (img.size[0]-1):
                if j == 0 or i == (img.size[1]-1):
                    for k in range(5):
                        r_values.append(0)
                        g_values.append(0)
                        b_values.append(0)
                else:
                    for k in range(3):
                        r_values.append(0)
                        g_values.append(0)
                        b_values.append(0)
            elif j == 0 or i == (img.size[1]-1):
                for k in range(3):
                    r_values.append(0)
                    g_values.append(0)
                    b_values.append(0)
            
            if i != 0:
                if j != 0:
                    # 0,0
                    r_values.append(pixelMap[i-1,j-1][0])
                    g_values.append(pixelMap[i-1,j-1][1])
                    b_values.append(pixelMap[i-1,j-1][2])
                # 0,1
                r_values.append(pixelMap[i-1,j][0])
                g_values.append(pixelMap[i-1,j][1])
                b_values.append(pixelMap[i-1,j][2])

                if j < (img.size[1] - 1):
                    # 0,2
                    r_values.append(pixelMap[i-1,j+1][0])
                    g_values.append(pixelMap[i-1,j+1][1])
                    b_values.append(pixelMap[i-1,j+1][2])
            
            if j != 0:
                # 1,0
                r_values.append(pixelMap[i,j-1][0])
                g_values.append(pixelMap[i,j-1][1])
                b_values.append(pixelMap[i,j-1][2])

            if j < (img.size[1] - 1):
                # 1,2
                r_values.append(pixelMap[i,j+1][0])
                g_values.append(pixelMap[i,j+1][1])
                b_values.append(pixelMap[i,j+1][2])
            
            if i < (img.size[0] - 1):
                if j != 0:
                    # 2,0
                    r_values.append(pixelMap[i+1,j-1][0])
                    g_values.append(pixelMap[i+1,j-1][1])
                    b_values.append(pixelMap[i+1,j-1][2])
            
                # 2,1
                r_values.append(pixelMap[i+1,j][0])
                g_values.append(pixelMap[i+1,j][1])
                b_values.append(pixelMap[i+1,j][2])
            
                if j < (img.size[1] - 1):
                    # 2,2
                    r_values.append(pixelMap[i+1,j+1][0])
                    g_values.append(pixelMap[i+1,j+1][1])
                    b_values.append(pixelMap[i+1,j+1][2])

            # CENTER #
            # 1,1
            r_values.append(pixelMap[i,j][0])
            g_values.append(pixelMap[i,j][1])
            b_values.append(pixelMap[i,j][2])

            r_values.sort()
            g_values.sort()
            b_values.sort()

            newMap[i,j] = (r_values[5], g_values[5], b_values[5])

    img2.show()
            
median(img, pixelMap)