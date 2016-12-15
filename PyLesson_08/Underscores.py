sentence = input("Please enter a string: ")

def replace():
    if sentence.count(" ") < 0: 
        return sentence
    else:
        print(sentence)
        replace((sentence[0:sentence.index(" ") + "_" + (sentence[sentence.index(" "): len(sentence))


replace()
