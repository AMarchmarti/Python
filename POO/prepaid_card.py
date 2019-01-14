from class_hour import Hour


class PrepaidCard:


    def __init__(self, phone, dni, balance):
        self.phone = phone
        self.dni = dni
        self.balance = balance

    
    def getPhone(self):
        return self.phone

    
    def getDni(self):
        return self.dni


    def depositBalance(self, value):
        self.balance += value
        return self.balance


    def sendMessage(self, numberMessage):
        cost = numberMessage * 0.09
        self.balance -= cost
        return self.balance
    

    def getBalance(self):
        return self.balance







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

    