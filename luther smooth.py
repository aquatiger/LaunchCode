# Doesn't work, but I need to move on. Will return sometime

import cImage

img = cImage.Image("luther.jpg")
lutherW = img.getWidth()
lutherH = img.getHeight()
newimg = cImage.EmptyImage(lutherW, lutherH)
win = cImage.ImageWin()

for col in range(img.getWidth()):
    for row in range(img.getHeight()):

            p = img.getPixel(col, row)
            if row == 0 or row == lutherH or col == 0 or col == lutherW:
                north = 0
                northeast = 0
                northwest = 0
                south = 0
                southeast = 0
                southwest = 0
                west = 0
                east = 0
                
            else:
                north = img.getPixel(col, row-1)
                south = img.getPixel(col, row+1)
                east = img.getPixel(col+1, row)
                west = img.getPixel(col-1, row)
                northeast = img.getPixel(col+1, row-1)
                northwest = img.getPixel(col-1, row-1)
                southeast = img.getPixel(col+1, row+1)
                southwest = img.getPixel(col+1, row-1)

# got a TypeError: unsupported operand type(s) for +: 'int' and 'Pixel'            
            newpixel = (north+south+east+west+northeast+southeast+southwest+northwest+p) / 9

## I get an IndexError if the row/col +1 or row/col -1 is outside the image
##            elif IndexError:
##                continue
newimg.setPixel(col, row, newpixel)
        

newimg.draw(win)
win.exitOnClick()
