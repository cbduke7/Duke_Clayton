sentence = input("Please enter a sentence: ")


def replace():
    while sentence.count("a") > 0:
        sentence = sentence[0 : sentence.index("a")] + sentence[sentence.index("@")+ 1 : len(sentence)]
        print(sentence)

replace()


    
