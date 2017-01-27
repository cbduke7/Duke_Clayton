class MilesPerHour:
    def __init__(self, distance, hours, minutes):
        self.distance = distance
        self.hours = hours
        self.minutes = minutes
        mph = 0
    
    def setValues(self, distance, hours, minutes):
        self.distance = distance
        self.hours = hours
        self.minutes = minutes
        mph = 0

    def getDist():
        return distance

    def getHours():
        return hours

    def getMins():
        return minutes

    def getMPH():
        mph = distance/(hours + minutes / 60.0)
        return mph
def main():
    distance = int(input("Enter a distance: "))
    hours = int(input("Enter an amount of hours: "))
    minutes = int(input("Enter the amount of minutes: "))
    mph = MilesPerHour(distance, hours, minutes)

    print(mph.distance(), "miles in", mph.hours(), "and", mph.minutes(), "=", mph.mph(),".")
        
main()    
    
    
    

    
