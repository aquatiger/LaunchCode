import cImage

img = cImage.Image("luther.jpg")
newimg = cImage.EmptyImage(img.getWidth(), img.getHeight())
win = cImage.ImageWin()

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)

        newred = 0
        green = p.getGreen()
        blue = p.getBlue()

        newpixel = cImage.Pixel(newred, green, blue)

        newimg.setPixel(col, row, newpixel)

newimg.draw(win)
win.exitonclick()
