sentence = input("Please enter a string: ")

def replace():
    global sentence
    if sentence.count(" ") < 0: 
        return sentence
    else:
        sentence = sentence[0 : sentence.index(" ")] + "_" + sentence[sentence.index(" ")+ 1 : len(sentence)]
        print(sentence)
        
replace()
