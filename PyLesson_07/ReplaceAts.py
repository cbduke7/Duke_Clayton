sentence = input("Please enter a sentence: ")


def replace():
    global sentence
    while sentence.count("a") > 0:
        sentence = sentence[0 : sentence.index("a")] + "@" + sentence[sentence.index("a")+ 1 : len(sentence)]
    print(sentence)

replace()


    
