def interest(r, p, n, t):
    return ((r / n + 1) ** (n * t) * p / (t * 12))
    
    
r = float(input("What is your interest rate? "))
p = int(input("What is your principal? "))
n = int(input("How many times is the loan compounded per year? "))
t = int(input("What is the life of the loan in years? "))



print("The monthly payment amount for the loan is $ {:.2f}".format(interest(r, p, n, t)), ".")
