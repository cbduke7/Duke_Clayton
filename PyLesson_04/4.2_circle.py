r = int(input("Please input the radius: "))

def calcArea(r):
    return (r ** 2) * 3.14

def display():
    print("The area of a circle with a radius", r, "is {:.5f}".format(calcArea(r)),".")

display()
