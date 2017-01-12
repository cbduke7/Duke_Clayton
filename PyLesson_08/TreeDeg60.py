word = input("Please enter a word: ")
stop = len(word)
start = 0

def tree(word, start, stop):
    if start <= stop:
        print(word[0:start])
        start += 1
        return tree(word, start, stop)
    else:
        return word

print(tree(word, start, stop))
