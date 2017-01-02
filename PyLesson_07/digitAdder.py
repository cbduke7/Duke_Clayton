<<<<<<< Updated upstream
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
=======
number = int(input("Please enter a number:" ))
sum = 0
num = number

def sumDigits():
    while number > 0:
        print (number % 10 + sum)
        num = int(num / 10)


sumDigits()

print("The sum of the digits in", number,"is", sum)
>>>>>>> Stashed changes
