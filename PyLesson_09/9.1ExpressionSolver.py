mathExpress = input("Please enter a mathematical expression: ")
equation = mathExpress.split(" ")

while (i < len(equation)):
    if ((i < len(equation)) and (equation[i] == "*" or "/")):
        if equation[i] == "*":
            equation[i] == int(equation([i]-1)) * int(i+1)
        else:
            equation[i] == int(equation([i]-1) / int(i+1)
        .remove(equation([i]-1))
        .remove(equation([i]))
    elif:
        1 += i
        
       
i = 0
while (i < len(equation)):
    if (i > len(equation)) and (equation[i] == "+" or "-"):
        if (equation[i] == "+"):
            equation[i] == int(equation([i]-1)) + int(equation([i]+1)
        else:
            equation[i] == int(equation([i]-1) - int(equation([i]+1)
    .remove(equation[i]-1)
    .remove(equation[i])
    elif:
        1 += i

print(equation)
            
        
                    
