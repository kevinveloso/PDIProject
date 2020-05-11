from PIL import Image

img = Image.open('imagem_teste.jpg')
pixelMap = img.load()

# Gray scale R
def gray_r(img, pixelMap):
    
    img2 = Image.new(img.mode, img.size)
    newMap = img2.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            newMap[i,j] = (pixelMap[i,j][0], pixelMap[i,j][0], pixelMap[i,j][0])

    img2.show()

# Gray scale G
def gray_g(img, pixelMap):
    
    img2 = Image.new(img.mode, img.size)
    newMap = img2.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            newMap[i,j] = (pixelMap[i,j][1], pixelMap[i,j][1], pixelMap[i,j][1])

    img2.show()

# Gray scale B
def gray_b(img, pixelMap):
    
    img2 = Image.new(img.mode, img.size)
    newMap = img2.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            newMap[i,j] = (pixelMap[i,j][2], pixelMap[i,j][2], pixelMap[i,j][2])

    img2.show()

# Mono R
def mono_r(img, pixelMap):
    
    img2 = Image.new(img.mode, img.size)
    newMap = img2.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            newMap[i,j] = (pixelMap[i,j][0], 0, 0)

    img2.show()

# Mono G
def mono_g(img, pixelMap):
    
    img2 = Image.new(img.mode, img.size)
    newMap = img2.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            newMap[i,j] = (0, pixelMap[i,j][1], 0)

    img2.show()

# Mono B
def mono_b(img, pixelMap):
    
    img2 = Image.new(img.mode, img.size)
    newMap = img2.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            newMap[i,j] = (0, 0, pixelMap[i,j][2])

    img2.show()

# Mono Roxo
def mono_purple(img, pixelMap):
    
    img2 = Image.new(img.mode, img.size)
    newMap = img2.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            newMap[i,j] = (pixelMap[i,j][2], 0, pixelMap[i,j][2])

    img2.show()

gray_b(img, pixelMap)       