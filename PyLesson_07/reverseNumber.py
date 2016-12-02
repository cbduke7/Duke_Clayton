number = int(input("Please enter a number: "))
num = number
rev = 0

def getReverse():
    while num > 0:
        global rev, num
        rev *= 10
        rev = (number % 10 + rev)
        num = int(num / 10)

getReverse()
print(number, "reversed is", rev)        
