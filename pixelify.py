from PIL import Image


DIM = int(input("what dimension would you like? "))


def getArea(img, starting_x, starting_y):
    total = [0,0,0]
    for i in range(starting_x, starting_x+DIM):
        for j in range(starting_y, starting_y + DIM):
            pixel = img.getpixel((i, j))
            for k in range(3):
                total[k] += pixel[k]
    for i in range(3):
        total[i] = total[i] // (DIM*DIM)
    return tuple(total)

def pixelify(filepath):
    img = Image.open(filepath).convert('RGB')
    numacross = int(img.width / DIM)
    numrows = (int)(img.height / DIM)
    outputimg = Image.new('RGB', (numacross*DIM, numrows*DIM))
    for x in range(0,numacross*DIM, DIM):
        for y in range(0,numrows*DIM,DIM):
            replacement_pixel = getArea(img,x,y)
            for output_x in range(x,x+DIM):
                for output_y in range(y,y+DIM):
                    outputimg.putpixel((output_x,output_y),replacement_pixel)
    outputimg.save("./images/output.png")

pixelify(input("relative filepath: "))
