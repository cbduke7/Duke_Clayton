sentence = input("Please enter a string: ")

def replacer():
    global sentence
    if sentence.count(" ") < 0: 
        return sentence
    else:
        return sentence * recur(sentence[0 : sentence.index(" ")] + "_" + sentence[sentence.index(" ")]
replacer()
