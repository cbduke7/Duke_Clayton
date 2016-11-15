word = input("Please enter a word: ")

for i in range(len(word), 0, -1):
    print(word[-i:len(word)])
