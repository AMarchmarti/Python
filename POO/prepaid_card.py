from class_hour import Hour


class PrepaidCard:


    def __init__(self, phone, dni, balance):
        self.phone = phone
        self.dni = dni
        self.balance = balance

    
    def getPhone(self):
        return str(self.phone)

    
    def getDni(self):
        return str(self.dni)


    def depositBalance(self, value):
        self.balance += value
        return self.balance


    def sendMessage(self, numberMessage):
        cost = numberMessage * 0.09
        self.balance -= cost
        return self.balance
    

    def callTime(self, seconds):
        hour = Hour(0, 0, seconds)
        Hour.setHour(hour)
        return hour.getHour()


    def makeCall(self, seconds):
        consum = 0.15 + (0.01 * seconds)
        self.balance -= consum
        return self.balance


    def getBalance(self):
        return self.balance


    def checkCard(self, seconds):
        balance = self.getBalance()
        print("Good morning, your phone number is %s with NIF: %s. Your balance is %s with call time of %s" % (self.getPhone(), self.getDni(), balance, self.callTime(seconds)))


if __name__ == "__main__":

    #Tests Cases
    card1 = PrepaidCard("645378955", "43425351F", 1000)
    assert card1.getPhone() == "645378955"
    assert card1.getDni() == "43425351F"
    assert card1.getBalance() == 1000
    #Test depositBalance
    card1.depositBalance(1000)
    assert card1.getBalance() == 2000
    #Tests sendMessage
    card1.sendMessage(200)
    assert card1.getBalance() == 1982
    #Test callTime
    assert card1.callTime(300) == "00:05:00"
    #Test makeCall
    card1.makeCall(300)
    assert card1.getBalance() == 1978.85
    #Test checkCard
    
    card1.checkCard(300)
    

    