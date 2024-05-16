from PIL import Image, ImageFilter
import cv2

'''
Create a blank sudoku puzzle'''

filename = "sudoku.png"

with Image.open(filename) as img:
    img.load()

# img.show()

print(img.size)
cropped = img.crop((19,470, 1230, 1730))
#cropped.show()

#cropped.show()

# img_gray = cropped.convert("L")
# # edges = img_gray.filter(ImageFilter.FIND_EDGES)
# # edges.show()

# img_gray.show()

square = cropped.crop((0,0,150,150))

row = 5
col = 4

square = cropped.crop((row*130, col*130, row*130+150, col*130+150))
square=square.resize((28,28))
square.show()