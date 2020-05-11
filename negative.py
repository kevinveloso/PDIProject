from PIL import Image

img = Image.open('negativeimg.jpg')
pixelMap = img.load()

# Negative
def negative(img, pixelMap):
    
    img2 = Image.new(img.mode, img.size)
    newMap = img2.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            newMap[i,j] = (255 - pixelMap[i,j][0], 255 - pixelMap[i,j][1], 255 - pixelMap[i,j][2])

    img2.show()

negative(img, pixelMap)