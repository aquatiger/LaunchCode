import cImage

img = cImage.Image("luther.jpg")
lutherW = img.getWidth() * 2
lutherH = img.getHeight() * 2
newimg = cImage.EmptyImage(lutherW, lutherH)
win = cImage.ImageWin()

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)

        newimg.setPixel(2*col, 2*row, p)
        newimg.setPixel(2*col, 2*row+1, p)
        newimg.setPixel(2*col+1, 2*row, p)
        newimg.setPixel(2*col+1, 2*row+1, p)


newimg.draw(win)
win.exitOnClick()
