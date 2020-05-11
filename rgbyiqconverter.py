from PIL import Image
import numpy as np

img = Image.open('imagem_teste.jpg')
pixelMap = img.load()

yiq_matrix = [[0.299, 0.587, 0.114],[0.596, -0.274, -0.322],[0.211, -0.523, 0.312]]
rgb_matrix = [[1.000, 0.956, 0.619],[1.000, -0.272, -0.647],[1.000, -1.106, 1.703]]

def keep_in_range(num):
    
    if num > 255:
        num = 255
    elif num < 0:
        num = 0
    
    return num

# RGB to YIQ Converter
def rgb_to_yiq(img, pixelMap):
    
    img2 = Image.new(img.mode, img.size)
    newMap = np.empty([img.size[0], img.size[1]], dtype = tuple)
    #newMap = img2.load()

    for k in range(img.size[0]):
        for j in range(img.size[1]):
            
            r = pixelMap[k,j][0]
            g = pixelMap[k,j][1]
            b = pixelMap[k,j][2]
            
            y = long(yiq_matrix[0][0] * r) + long(yiq_matrix[0][1] * g) + long(yiq_matrix[0][2] * b)
            i = long(yiq_matrix[1][0] * r) + long(yiq_matrix[1][1] * g) + long(yiq_matrix[1][2] * b)
            q = long(yiq_matrix[2][0] * r) + long(yiq_matrix[2][1] * g) + long(yiq_matrix[2][2] * b)

            newMap[k,j] = (int(y), int(i), int(q))
    #img2.show()
    return newMap

#YIQ to RGB Converter
def yiq_to_rgb(matrix):
    img2 = Image.new(img.mode, matrix.shape)     
    newMap = img2.load()

    for k in range(img2.size[0]):
        for j in range(img2.size[1]):       
            y = matrix[k,j][0]
            i = matrix[k,j][1]
            q = matrix[k,j][2]
            
            r = keep_in_range(y + long(rgb_matrix[0][1] * i) + long(rgb_matrix[0][2] * q))
            g = keep_in_range(y + long(rgb_matrix[1][1] * i) + long(rgb_matrix[1][2] * q))
            b = keep_in_range(y + long(rgb_matrix[2][1] * i) + long(rgb_matrix[2][2] * q))

            newMap[k,j] = (r, g, b)
    img2.show()

yiq_to_rgb(rgb_to_yiq(img, pixelMap))
#rgb_to_yiq(img, pixelMap)