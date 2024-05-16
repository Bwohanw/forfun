from PIL import Image


def sqdistance(pixel1, pixel2):
    dist = 0
    for i in range(3):
        dist += (pixel1[i]-pixel2[i])**2
    return dist

def maketransparent(filename, threshold=0):
    filepath = './images/' + filename
    whitepixel = (255,255,255,255)
    try:
        img = Image.open(filepath).convert('RGBA')
    except:
        print('No image found')
        return
    pixels = list(img.getdata())
    print(pixels[0])
    for i in range(img.height):
        finishedrow = True
        for j in range(img.width):
            if (sqdistance(pixels[i*img.width + j], whitepixel) <= threshold):
                pixel = pixels[i*img.width + j]
                pixels[i*img.width + j] = tuple([pixel[0],pixel[1],pixel[2],0])
            else:
                finishedrow = False
                break
        if not finishedrow:
            for j in range(img.width-1, -1, -1):
                pixel = pixels[i*img.width + j]
                if (sqdistance(pixel,whitepixel) <= threshold):
                    pixels[i*img.width + j] = tuple([pixel[0],pixel[1],pixel[2],0])
                else:
                    break
    for i in range(img.width):
        finishedcol = True
        for j in range(img.height):
            pixel = pixels[j*img.width + i]
            if (sqdistance(pixel, whitepixel) <= threshold):
                pixels[j*img.width + i] = tuple([pixel[0],pixel[1],pixel[2],0])
            else:
                finishedcol = False
                break
        if not finishedcol:
            for j in range(img.height-1,-1,-1):
                pixel=pixels[j*img.width + i]
                if (sqdistance(pixel,whitepixel)<=threshold):
                    pixels[j*img.width + i] = tuple([pixel[0],pixel[1],pixel[2],0])
                else:
                    break
    outputimg = Image.new(img.mode,img.size)
    print(pixels[0])
    outputimg.putdata(pixels)
    outputimg.save('./images/output.png')
    return

maketransparent('business.png', threshold=3000)
