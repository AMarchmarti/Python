class Data:

    def __init__(self, day, month, year):
        try:
            self.day = day
            self.month = month
            self.year = year   
            assert self.day in range(1, 32) and self.month in range(1,13) and self.year in range(1900, 3001)
        except AssertionError:
            self.day = 1
            self.month = 1
            self.year = 1900


    def setDay(self, day):
        assert self.day in range(1,32)
        try:
            self.day = day
        except AssertionError:
            self.day = 1
    def getDay(self, day):
        return self.day

    def setMonth(self, month):
        assert self.month in range(1,13)
        try:
            self.month = month
        except AssertionError:
            self.month = 1
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

    """
    def setDate(self, day, month, year):
        assert self.day in range(1, 32) and self.month in range(1,13) and self.year in range(1900, 3001)
        try:
            self.day = day
            self.month = month
            self.year = year   
        except AssertionError:
            self.day = 1
            self.month = 1
            self.year = 1900
    """
    
    def addDays(self, numberdays):

        try:
            while numberdays > 0:
                self.day += 1
                if self.day > 31:
                    self.day = 1
                    self.month += 1
                    if self.month > 12:
                        self.month = 1
                        self.year += 1
                numberdays -= 1
            assert self.year in range(1900, 3001)
        except AssertionError:
            self.day = 1
            self.month = 1
            self.year = 1900
        except ValueError:
            print("%s not an integer" % numberdays)

    
    def __monthLetter(self):
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        keyMonth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        
        numbermonth = dict(zip(keyMonth, months))
        assert isinstance(numbermonth, dict)
        assert numbermonth[6] == "June"

        if self.month in numbermonth:
            self.month = numbermonth[self.month]
        return self
        

    def getDate(self):
        return str(self.day) + "-" + self.month + "-" + str(self.year)
        
    
    def printDate(self):
        item = self.__monthLetter()
        item = self.getDate()
        print(item)
        return item

if __name__ == "__main__":

    #Tests Cases

    data = Data(13, 4, 2030)
    assert data.printDate() == "13-April-2030"

    data2 = Data(14, 5, 2021)
    assert data2.printDate() == "14-May-2021"

    data3 = Data(21, 11, 2050)
    data3.addDays(1000)
    assert data3.printDate() == "29-July-2053"





                
    



    
