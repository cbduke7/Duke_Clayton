
length = int(input("Please enter the length of the rectangle: "))
width = int(input("Please enter the width of the rectangle: "))

def calcPerim(length, width):
    return length + width * 2

def perimter():
    print("Your perimeter is {:.5f}".format(calcPerim(length, width)),"ft around.")

perimter()
