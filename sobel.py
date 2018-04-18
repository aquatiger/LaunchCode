# My feeble attempt at implemeting a Sobel algorithm including mostly pseudocode
import math

a = img.getPixel(col, row)

# not sure how to do matrices in python here
gSubX = 1 * a + 0 + (-1 * a)
gSubY = 

# the gradient magnitude
gradient = math.sqrt(gSubX ** 2 + gSubY ** 2)

# calculating the gradient's direction
# atan is returned in radians
theta = math.atan(gSubY / gSubX)

