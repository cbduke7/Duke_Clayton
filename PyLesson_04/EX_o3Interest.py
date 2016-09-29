def interest(r, p, n, t):
    return ((r/100 / n + 1) ** (n * t) * p)
    
    
r = float(input("What is your interest rate? "))
p = int(input("What is your principal? "))
n = int(input("How many times is the loan compounded per year? "))
t = int(input("What is the life of the loan in years? "))



print("The total cost of the loan is $ {:.2f}".format(interest(r, p, n, t)), ".")
