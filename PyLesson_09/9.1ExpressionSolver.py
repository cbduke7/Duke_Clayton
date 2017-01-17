mathExpess = input("Please enter a mathematical expression: ")
equation = word.split(" ")

while i < len(equation):
    if i < len(equation) and (equation(i) == "*" or "/"):
        if equation(i) == "*":
            equation(i) == int(equation(i-1) * int(i+1)
        else:
            equation(i) == int(equation(i-1) / int(i+1)
            nums.remove(equation(i-1))
            nums.remove(i)
    else:
        1 += i

