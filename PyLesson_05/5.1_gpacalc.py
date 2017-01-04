def clps(grde):
    if grde == "A":
        return 4.0
    elif grde == "B":
        return 3.0
    elif grde == "C":
        return 2.0
    elif grde == "D":
        return 1.0
    elif grde == "F":
        return 0.0
    
lg1 = input("Please enter your letter grade for math: ")
lg2 = input("Please enter your letter grade for science: ")
lg3 = input("Please enter your letter grade for history: ")
lg4 = input("Please enter your letter grade for english: ")
lg5 = input("Please enter your letter grade for computer programming: ")
lg6 = input("Please enter your letter grade for your language: ")
lg7 = input("Please enter your letter grade for another elective: ")


print("Your GPA is", (clps(lg1) + clps(lg2) + clps(lg3) + clps(lg4) + clps(lg5) + clps(lg6) + clps(lg7)) / 7) 
