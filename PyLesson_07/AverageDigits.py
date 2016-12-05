number = int(input("Please enter a number: "))
digits = 0
average = 0

def avDigits():
    num = number
    global digits, average
    while num > 0:
        digits = (1 + digits)
        average = (number %10 + average)
        num = int(num/10)
avDigits()
print("The average of the digits in", number,"is", average)
