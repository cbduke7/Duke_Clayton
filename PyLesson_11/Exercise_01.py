class MilesPerHour:
    def __init__(self, dist=0, hours=0, mins=0):
        self.distance = dist
        self.hours = hours
        self.minutes = mins
        mph = 0
    
    def setValues(self, dist, hours, mins):
        self.distance = dist
        self.hours = hours
        self.minutes = mins
        mph = 0

    def getDist(self):
        return self.distance

    def getHours(self):
        return self.hours

    def getMins(self):
        return self.minutes

    def getMPH(self):
        mph = distance/ (hours + minutes / 60.0)
        return self.mph
def main():
    distance = input("Enter a distance: ")
    hours = input("Enter an amount of hours: ")
    minutes = input("Enter the amount of minutes: ")
    mph = MilesPerHour(distance, hours, minutes)

    print(mph.getDist(), "miles in", mph.getHours(), "and", mph.getMins(), "=", mph.getMPH(),".")
    

    
main()    
    
    
    

    
