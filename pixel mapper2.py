import cImage

def pixelMapper(oldimage, rgbFunction):
    width = oldimage.getWidth()
    height = oldimage.getHeight()
    newim = cImage.EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            originalpixel = oldimage.getPixel(col, row)
            newpixel = rgbFunction(originalpixel)
            newim.setPixel(col, row, newpixel)
# Why does return work when I copy code, but not when I write it myself?
    return newim

def graypixel(oldpixel):
    intensitysum = oldpixel.getRed() + oldpixel.getGreen() + oldpixel.getBlue()
    aveRGB = intensitysum // 3
    newPixel = cImage.Pixel(aveRGB, aveRGB, aveRGB)
# Same question
    return newPixel

win = cImage.ImageWin()
img = cImage.Image("luther.jpg")

newim = pixelMapper(img, graypixel)
newim.draw(win)

win.exitonclick()
