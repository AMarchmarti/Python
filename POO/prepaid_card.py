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


    def getSaldo(self):
        return self.getSaldo







if __name__ == "__main__":

    #Tests Cases
    card1 = PrepaidCard("645378955", "43425351F", 1000)
    assert card1.getPhone() == "645378955"
    