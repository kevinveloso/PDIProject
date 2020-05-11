from PIL import Image

img = Image.open('imagem_teste.jpg')
pixelMap = img.load()

def keep_in_range(num):
    
    if num > 255:
        num = 255
    elif num < 0:
        num = 0
    
    return num

# Aditive
def add_brightness(level, img, pixelMap):
    
    img2 = Image.new(img.mode, img.size)
    newMap = img2.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            
            r = keep_in_range(level + pixelMap[i,j][0])
            g = keep_in_range(level + pixelMap[i,j][1])
            b = keep_in_range(level + pixelMap[i,j][2])

            newMap[i,j] = (r, g, b)

    img2.show()

# Multiplicative
def mult_brightness(level, img, pixelMap):
    
    img2 = Image.new(img.mode, img.size)
    newMap = img2.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            
            r = keep_in_range(round(level * pixelMap[i,j][0]))
            g = keep_in_range(round(level * pixelMap[i,j][1]))
            b = keep_in_range(round(level * pixelMap[i,j][2]))

            newMap[i,j] = (int(r), int(g), int(b))

    img2.show()

add_brightness(100, img, pixelMap)