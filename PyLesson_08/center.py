word1 = input("Please enter a word: ")
word2 = input("Please enter a word: ")
word3 = input("Please enter a word: ")

def makeCenter(word):
    if len(word) >= 20:
        return word
    else:
<<<<<<< Updated upstream
        return makeCenter(" " + word + " ")
=======
        makeCenter(" " + word + " ")
>>>>>>> Stashed changes
        
        

print(makeCenter(word1))
print(makeCenter(word2))
print(makeCenter(word3))
