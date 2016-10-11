def format(item, price):
    print("*{:^15}.....\t{:7.2f}".format(item, price))

def discount():
    if subtotal >= 2000:
        discount = 15
    if subtotal < 2000:
        discount = 0

item1 = input("Please enter item 1:")
price1 = float(input("Please enter the price:"))
item2 = input("Please enter item 2:")
price2 = float(input("Please enter the price:"))
item3 = input("Please enter item 3:")
price3 = float(input("Please enter the price:"))


subtotal = (price1 + price2 + price3)
discount()
disamount = (subtotal * (100 * discount))
tax = (subtotal * .075)
total = (subtotal + tax - disamount)


print("<<<<<<<<<<__Receipt__>>>>>>>>>>")
format(item1, price1)
format(item2, price2)
format(item3, price3)
format("Subtotal: ", subtotal)
format("Discount: ", discount,"%")
format("Tax: ", tax)
format("Total: ", total)
print("_______________________________")
print( "* Thank you and come again *")
