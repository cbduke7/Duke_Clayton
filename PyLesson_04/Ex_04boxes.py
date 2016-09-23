def volume(height, length, width):
    return((height * length * width) * 1728)
    

height = int(input("Please enter the height of the box: "))
length = int(input("Please enter the length of the box: "))
width = int(input("Please enter the width of the box: "))

print("The volume is ",volume(height, length, width), "cubic feet")
