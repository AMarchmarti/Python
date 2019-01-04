class CurrentAccount:

    def __init__(self, name, surname, direction, phone, balance):
        self.name = name
        self.surname = surname
        self.direction = direction
        self.phone = phone
        self.balance = balance

    

    def setWithdrawBalance(self, amount):
        self.balance -= amount
        return self.balance

    def setDepositMoney(self, amount):
        self.balance += amount
        return self.balance
        

    def getbankruptcy(self):
        if self.balance < 0:
            return True
        return False
    
    def checkAccount(self):
        for element in self.__dict__:
            print("%s : %s" % (element, self.__dict__[element]))

if __name__ == "__main__":

    account_Juan = CurrentAccount("Juan", "Gomez Serna", "Vall d'argent nº27", "678945610", 400)
    account_Juan.checkAccount()

    account_Tommy = CurrentAccount("Tommy", "Strange", "Baker street", "113425978", 1000)
    account_Tommy.checkAccount()
    assert account_Tommy.setWithdrawBalance(500) == 500
    assert account_Tommy.setDepositMoney(1000) == 1500
    assert account_Tommy.getbankruptcy() == False
    account_Tommy.checkAccount()
    
    


        