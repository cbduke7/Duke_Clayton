sentence = input("Please enter a string: ")

def replace(sentence):
    if sentence.count(" ") == 0: 
        return sentence
    else:
        replace((sentence[0:sentence.index(" ")]) + "_" + (sentence[sentence.index(" ")+1: len(sentence)]))
        print(sentence)    

replace(sentence)


