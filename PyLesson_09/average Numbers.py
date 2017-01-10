numbers = []
import random
for i in range(0, 10):
    numbers.append(random.randint(1, 100))

print(numbers)

output = ""
j = 0

for i in numbers:
    output += str(i) + " "
    if j < len(numbers):
        output += ", "
    j += 1

def average(numbers):
    s = 0
    for i in numbers:
        s += (i)
    return s/10
    
print(output)
print("")
print("The average of the above numbers is ...", average(numbers))


        
