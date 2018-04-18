import cImage

img = cImage.Image("luther.jpg")
newimg = cImage.EmptyImage(img.getWidth(), img.getHeight())
win = cImage.ImageWin()

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)

        red = p.getRed()
        green = p.getGreen()
        blue = p.getBlue()
        new_value = (red + green + blue) / 3
        white = cImage.Pixel(255, 255, 255)
        black = cImage.Pixel(0, 0, 0)
        
        if new_value <(255/2):
            newimg.setPixel(col, row, black)
        else:
            newimg.setPixel(col, row, white)

newimg.draw(win)

