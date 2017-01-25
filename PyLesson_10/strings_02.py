go = input("Please enter 16 strings: ")
spList = go.split(" ")
wordsList = []
spot = 0

for i in range(0, 4):
    output = ""
    wordsList.append([])
    for i in range(0, 4):
        wordsList[i] += spList[spot]
        output += wordsList[i][0]
        spot += 1
    print(output)
