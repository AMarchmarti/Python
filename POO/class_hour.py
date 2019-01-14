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
            self.hour += (int(self.minutes / 60))
            self.minutes = self.minutes % 60
        elif self.seconds not in range(0, 59):
            self.minutes += (int(self.seconds / 60))
            self.seconds = self.seconds % 60

    
    def getHour(self):
        return "%02d:%02d:%02d" % (self.hour, self.minutes, self.seconds)


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
    assert Hour.getHour(hour2) == "00:00:34"