side = 4
sa = 0

def setNum():
    global side
    side = 8

def calcSurf():
    global sa
    sa = (side ** 2) * 6

setNum()
calcSurf()


print("The surface area of a cube whose sides are", side, "in length is {:.5f}".format(sa),".")


