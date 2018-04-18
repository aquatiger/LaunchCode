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
        newR = int((red * 0.393 + green * 0.769 + blue * 0.189))
        newG = int((red * 0.349 + green * 0.686 + blue * 0.168))
        newB = int((red * 0.272 + green * 0.534 + blue * 0.131))
        sepia = cImage.Pixel(newR, newG, newB)

        newimg.setPixel(col, row, sepia)

newimg.draw(win)

##sepia tone formula from interactivepython.org
##newR = (R × 0.393 + G × 0.769 + B × 0.189)
##newG = (R × 0.349 + G × 0.686 + B × 0.168)
##newB = (R × 0.272 + G × 0.534 + B × 0.131)

