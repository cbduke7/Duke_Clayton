import random
class User:
   def __init__(self, fName, lName, avat = ""):
       self.firstName = fName
       self.lastName = lName
       self.avatar = avat
       self.userID = random.randint(0, 1000000)


       def setAvatar(self, avat):
           self.avatar = avat

        
       def getAvatar(self):
           return self.avat

       def getFirstName(self):
           return self.fName

       def getLastName(self):
           return self.lName

       def getUserID(self):
           return self.userID



def main():
    fName = input("Please enter your first name: ")
    lName = input("Please enter your last name: ")
    prompt = input("Would you like to use a public avatar?(yes or no) ")

    if prompt == "no" or "No" or "n":
        user1 = User(fName, lName)
    if prompt == "yes" or "Yes" or "y":
        avatar = input("Ente your avatar name: ")
        user1 = User(fName, lName, avatar)
        print(user1)
def __str__(self):
   return "Customer Info...\nFirst Name: " + self.firstName + \
          "\nLast Name: " + self.lastName + \
          "\nAvatar: " + self.avatar + \
          "\nUser ID#: " + str(self.userID)

    
main()
__str__()
