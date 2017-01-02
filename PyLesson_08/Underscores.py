sentence = input("Please enter a string: ")

<<<<<<< Updated upstream
def replace(sentence):
    if sentence.count(" ") == 0: 
        return sentence
    else:
        replace((sentence[0:sentence.index(" ")]) + "_" + (sentence[sentence.index(" ")+1: len(sentence)]))
        print(sentence)    

replace(sentence)


=======
def replace(sentence, new, old):
    if sentence.count(old) < 0: 
        return sentence
    else:
        return replace(sentence[0 : sentence.index(old)] + new + sentence[sentence.index(old) + 1 : len(sentence)])

replace(sentence, "_", " ")
>>>>>>> Stashed changes
