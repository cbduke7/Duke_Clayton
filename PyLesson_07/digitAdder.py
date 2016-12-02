number = int(input("Please enter a number:" ))
s = 0
num = number

def addDigits():
    while number > 0:
        global s, num
        s = (number % 10 + s)
        num /= 10

addDigits()

print("The sum of the digits in", number,"is", s)
