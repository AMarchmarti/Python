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
        assert self.hour in range(0,24) and self.minutes in range(0,59) and self.seconds in range(0, 59)
        try:
            return self
            
        except AssertionError:
            return 0

    
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
    assert Hour.getHour(hour2) == "0"