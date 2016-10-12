letterGrade1 = input("Please enter your letter grade for math: ")
letterGrade2 = input("Please enter your letter grade for science: ")
letterGrade3 = input("Please enter your letter grade for history: ")
letterGrade4 = input("Please enter your letter grade for english: ")
letterGrade5 = input("Please enter your letter grade for computer programming: ")
letterGrade6 = input("Please enter your letter grade for your language: ")
letterGrade7 = input("Please enter your letter grade for another elective: ")

def calcPoints():
    global letterGrade1, letterGrade2, letterGrade3, letterGrade4, letterGrade5, letterGrade6, letterGrade7
    if letterGrade1 == "A" or "a":
        return "4.0"
    if letterGrade1 == "B" or "b":
        return "3.0"
    if letterGrade1 == "C" or "c":
        return "2.0"
    if letterGrade1 == "D" or "d":
        return "1.0"
    if letterGrade1 == "F" or "f":
        return "0"

calcPoints()
gpa = ((letterGrade1 + letterGrade2 + letterGrade3 + letterGrade4 + letterGrade5 + letterGrade6 + letterGrade7) / 7)

print("Your GPA is", gpa)
