num1 = int(input("Please enter number 1: "))
num2 = int(input("Please enter number 2: "))
num3 = int(input("Please enter number 3: "))

def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

def display():
    print("The avereage of", num1,",", num2,",", "and", num3, "is {:.5f}".format(average(num1, num2, num3)),".")


display()
