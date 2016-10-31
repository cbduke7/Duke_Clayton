num1 = 13
num2 = 12
num3 = 6
avg = 0

def setNums():
    global num1, num2, num3
    num1 = 4
    num2 = 12
    num3 = 24

def average():
    global avg
    avg = (num1 + num2 + num3) / 3

setNums()
average()

print("The avereage of", num1,",", num2,",", "and", num3, "is {:.5f}".format(avg),".")


