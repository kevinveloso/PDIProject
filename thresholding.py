from PIL import Image

img = Image.open('spacesuit.0.jpg')
pixelMap = img.load()

def thresholding(img, pixelMap, m):
        
    img2 = Image.new(img.mode, img.size)
    newMap = img2.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):

            if pixelMap[i,j][1] > m:
                newMap[i,j] = (255, 255, 255)
            else:
                newMap[i,j] = (0, 0, 0)

    img2.show()

thresholding(img, pixelMap, 127)