sentence = input("Please enter a string: ")

def replace(sentence):
    if sentence.count(" ") < 0: 
        return sentence
    else:
        print(sentence)
        replace((sentence.index(" ") - 1) + "_" + (sentence.index(" ") + 1)) 


replace(sentence)
