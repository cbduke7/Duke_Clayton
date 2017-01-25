numsList = []


for i in range(0, 4):
    numsList.append([])
    for i in range(0, 4):
        import random
        numsList.append([i + (random.randint(0,100))])
        

for nums in numsList:
    output = ""
    for num in nums:
        output += str(num) + " "
    print(output)


