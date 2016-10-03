
length = int(input("Please enter the length of the rectangle: "))
width = int(input("Please enter the width of the rectangle: "))
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

print("Your perimeter is {:.5f}".format(perimeter),"ft around.")


