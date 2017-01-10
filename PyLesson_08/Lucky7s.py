number = int(input("Please enter a number: "))

def luck(number):
    if (number > 0):
        if ((number %10) == 7):
            return 1 + luck(number / 10)
        else:
            return 0 + luck(number / 10)
    else:
        return 0

luck(number)
