import random
class inventory():
    def __inti__(self, m, n, c, p):
        m = input("Please enter the manufacturer of the item: ")
        n = input("Please enter the name of the item: ")
        self.manufacturer = m
        self.name = n
        self.category = c
        self.price = p
        self.UPC = random.randint(0, 10000000000)

   
        
    
