side = int(input("Please input the value of the side: "))

def calcSurf(side):
    return (side ** 2) * 6

def display():
    print("The surface area of a cube whose sides are", side, "in length is {:.5f}".format(calcSurf(side)),".")

display()
