side = int(input("Please input the value of the side: "))
sa = 0

def calcSurf(side):
    global sa
    sa = (side ** 2) * 6

def display():


print("The surface area of a cube whose sides are", side, "in length is {:.5f}".format(calcSurf(side)),".")


