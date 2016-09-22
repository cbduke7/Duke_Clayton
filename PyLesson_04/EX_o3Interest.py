def interest(r ,p, n, t):
    return (p * (1 + r / n) ** (n * t)
    

r = int(input("What is your interest rate? "))
p = int(input("What is your principal? "))
n = int(input("How many times is the loan compounded per year? "))
t = int(input("What is the life of the loan in years"))



print("The total cost of the loan is $",interest(r ,p, n, t))
