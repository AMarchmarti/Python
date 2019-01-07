class Data:

    def __init__(self, day, month, year):
        self.day = "%02d" % int(1)
        self.month = "%02d" % int(1)
        self.year = 1900


    def setDay(self, day):
        assert self.day in range(1,32)
        try:
            self.day = day
        except AssertionError:
            self.day = "%02d" % int(1)
    def getDay(self, day):
        return self.day

    def setMonth(self, month):
        assert self.month in range(1,13)
        try:
            self.month = month
        except AssertionError:
            self.month = "%02d" % int(1)
    def getMonth(self, month):
        return self.month

    def setYear(self, year):
        assert self.year in range(1900,3001)
        try:
            self.year = year
        except AssertionError:
            self.year = year
    def getYear(self, year):
        return self.year


    def setDate(self, day, month, year):
        assert self.day in range(1, 32) and self.month in range(1,13) and self.year in range(1900, 3001)
        try:
            self.day = day
            self.month = month
            self.year = year   
        except AssertionError:
            self.day = "%02d" % int(1)
            self.month = "%02d" % int(1)
            self.year = 1900

    
    def addDays(self, numberdays):
        try:
            for number in range(1, numberdays + 1):
                self.day += number
                if self.day > 31:
                    self.day = 1
                    self.month += 1
                    if self.month > 12:
                        self.month = 1
                        self.year += 1
            assert self.year in range(1900, 3001)
        except AssertionError:
            self.day = "%02d" % int(1)
            self.month = "%02d" % int(1)
            self.year = 1900
        except ValueError:
            print("%s not an integer" % numberdays)

    
    def __monthLetter(self):
        months = ["January", "February", "March", "April", "May", "June", "July", ""]

    
