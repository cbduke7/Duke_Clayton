number = int(input("Please enter a number: "))
sum = 0
num = (number)

def sumDigits():
    global sum, num
    while num > 0:
        sum = (number %10 + sum)
        num = int(num/10)

sumDigits()
print("The sum of the digits in",number,"is",sum)
