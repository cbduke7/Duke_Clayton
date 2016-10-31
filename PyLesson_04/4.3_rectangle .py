length = 32
width = 14
perimeter = 0

def setDims():
    global length, width
    length = 8
    width = 4

def calcPerimeter():
    global perimeter
    perimeter = (length + width) * 2

setDims()
calcPerimeter()

print("Your rectangle is {:.5f}".format(perimeter),"ft around.")


