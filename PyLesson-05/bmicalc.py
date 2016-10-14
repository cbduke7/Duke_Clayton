height = int(input("What is your height in inches? "))
weight = int(input("What is your weight in lbs? "))
bmi = 0

def calcBMI():
    global bmi
    bmi = ((weight / (height**2)) * 703)

def condition():
    if bmi < 18.5:
        print("You are underweight")
    elif bmi >= 18.5:
        print("You are normal")
    elif bmi < 24.9:
        print("You are normal")
    elif bmi >= 25:
        print("You are overweight")
    elif bmi < 29.9:
        print("You are overweight")
    elif bmi >= 29.9:
        print("You are obese")
    elif bmi < 34.9:
        print("You are obese")
    elif bmi >= 35:
        print("You are very obese")
    elif bmi < 39.9:
        print("You are very obese")
    elif bmi > 39.9:
        print("You are morbidly obese")

calcBMI()
print("Your bmi is: {:.2f}".format(bmi))
condition()





