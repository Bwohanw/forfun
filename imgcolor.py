from PIL import Image

img = Image.open("Adobe Express - file.png")
width = img.width
height = img.height
for i in range(img.width):
    for j in range(img.height):
        pixel = img.getpixel((i,j))
        print(pixel)

