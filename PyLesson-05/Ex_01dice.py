import random
pRoll = random.randint(1, 6)
cRoll = random.randint(1, 6)

def rollDice():
    print("If you roll higher than the comuter \n \t You are the winner")
    print("If the computer rolls higher than you \n \t The computer is the winner \n")

rollDice()

print("Your number is", pRoll)
print("The computer's number is", cRoll)
if pRoll > cRoll:
    print("Congradulations, you win!")
if pRoll < cRoll:
    print("Sorry, the computer wins. Better luck next time.")
if pRoll == cRoll:
    print("You and the computer draw. Your not a looser but your still not a winner.")



