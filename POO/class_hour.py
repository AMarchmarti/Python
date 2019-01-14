class Hour:


    def __init__(self, hour, minutes, seconds):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds


    def getMinutes(self):
        return self.minutes

    
    def getSeconds(self):
        return self.seconds

    
    def setHour(self):
        if self.hour not in range(0, 24):
            self.hour = 0
        elif self.minutes not in range(0, 59):
            self.hour += 1
            self.minutes = 0
        elif self.seconds not in range(0, 59):
            self.minutes += 1
            self.seconds = 0

    
    def getHour(self):
        return "%s:%s:%s" % (self.hour, self.minutes, self.seconds)


    def printHour(self):
        time = self.getHour
        print(time)
        


if __name__ == "__main__":

    #Tests Cases

    hour1 = Hour(23,55,35)
    Hour.setHour(hour1)
    assert Hour.getHour(hour1) == "23:55:35"

    hour2 = Hour(25, 00, 34)
    Hour.setHour(hour2)
    assert Hour.getHour(hour2) == "0:0:34"