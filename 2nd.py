from PIL import Image

img = Image.open('lena.bmp')
pixelMap = img.load()

img2 = Image.new(img.mode, img.size)
newMap = img2.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        
        e = 0
        for n in range(samples_n - 1):
            e += samples[n] * math.cos((2 * math.pi * n * k)/(2 * samples_n) + (k * math.pi)/(2 * samples_n))

        if k == 0:
            c = math.sqrt(1/2)
        else:
            c = 1

        new_samples[k]  = math.sqrt(2/samples_n) * c * e