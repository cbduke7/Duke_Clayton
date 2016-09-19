item1 = input("Please enter item 1:")
price1 = int(input("Please enter the price:"))
item2 = input("Please enter item 2:")
price2 = int(input("Please enter the price:"))
item3 = input("Please enter item 3:")
price3 = int(input("Please enter the price:"))

def printf(word, number):
    print("{:<20}\t{:10.2f}".format(word, number))

print("<<<<<<<<<<<<__Receipt__>>>>>>>>>>>>")

   
word = item1
number = price1

printf(word, number)

word = item2
number = price2

printf(word, number)

word = item3
number = price3

