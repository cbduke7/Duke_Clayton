r = 3
area = 0

def setr():
    global r
    r = 9
    
def calcArea():
    global area
    area = (r ** 2) * 3.14

setr()
calcArea()

print("The area of a circle with a radius", r, "is {:.5f}".format(area),".")


