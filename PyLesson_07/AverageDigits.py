number = int(input("Please enter a number: "))
digits = 0
average = 0

def avDigits():
    num = number
    while num > 0:
        global digits, average, num
        digits += 1
        average = (number % 10 + average)
        num /= 10

avDigits()        
print("The average of the digits in",number,"is",average)
