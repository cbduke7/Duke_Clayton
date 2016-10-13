def clps(grde):
    if grde == "A" or "a":
        return 4.0
    if grde == "B" or "b":
        return 3.0
    if grde == "C" or "c":
        return 2.0
    if grde == "D" or "d":
        return 1.0
lg1 = input("Please enter your letter grade for math: ")
lg2 = input("Please enter your letter grade for science: ")
lg3 = input("Please enter your letter grade for history: ")
lg4 = input("Please enter your letter grade for english: ")
lg5 = input("Please enter your letter grade for computer programming: ")
lg6 = input("Please enter your letter grade for your language: ")
lg7 = input("Please enter your letter grade for another elective: ")

print("Your GPA is", (clps(lg1)+clps(lg2)+clps(lg3)+++++)/7)
