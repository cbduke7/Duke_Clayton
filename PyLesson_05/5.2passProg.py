password = ("Unicorn")
username = ("Choclate")

def passCheck():
    user = input("Please enter the username: ")
    passW = input("Please enter the password: ")
    if user == username and passW == password:
        print("The password is correct")
    else:
        if user == username:
            print("The password is incorrect!")
        elif passW == password:
            print("The username is incorrect")
        else:
            print("Your username and password are incorrect! ")

passCheck()
    
            
        
   
