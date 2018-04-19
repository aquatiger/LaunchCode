subtotal = [15, 16, 18, 23, 25]
total = [18, 19, 200, 341, 6]

for i in subtotal:
    for j in total:
        print('Total is: {}; \tSubtotal is: {};\t Average is: {:.2f}.'.format(i, j, (i+j)/((2))))
