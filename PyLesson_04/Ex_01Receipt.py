def format(item, price):
    print("{*:<1}{:^15}\t{:10.2f}".format(item, price))

item1 = input("Please enter item 1:")
price1 = float(input("Please enter the price:"))
item2 = input("Please enter item 2:")
price2 = float(input("Please enter the price:"))
item3 = input("Please enter item 3:")
price3 = float(input("Please enter the price:"))

subtotal = (price1 + price2 + price3)
tax = (subtotal * .075)
total = (subtotal + tax)

print("<<<<<<<receipt>>>>>>")
format(item1, price1)
format(item2, price2)
format(item3, price3)
format("Subtotal: ", subtotal)
format("Tax: ")
format("Total: ")
