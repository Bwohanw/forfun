from PIL import Image


RESIZE = 256

img = Image.open('flashcards.png')
new_img = img.resize((RESIZE, RESIZE))
new_img.save('./temp/flashcards' + str(RESIZE) + '.png')