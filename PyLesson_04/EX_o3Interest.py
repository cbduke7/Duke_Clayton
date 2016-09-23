def interest(r, p, n, t):
    return ((r / n + 1) ** (n * t) * p)

r = float(input("What is your interest rate as a deimal? "))
p = int(input("What is your principal? "))
n = int(input("How many times is the loan compounded per year? "))
t = int(input("What is the life of the loan in years? "))



print("The total cost of the loan is $",interest(r, p, n, t))
