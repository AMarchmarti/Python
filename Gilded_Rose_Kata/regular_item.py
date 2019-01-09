from interface_updatable import Updatable
from item import Item


class RegularItem(Item, Updatable):


    def setSell_in(self):
        self.sell_in = self.sell_in - 1
    

    def setQuality(self, valor):

        if self.quality + valor > 50:
            self.quality = 50
        elif self.quality + valor >= 0:
            self.quality = self.quality + valor
        else:
            self.quality = 0
    

    def update_quality(self):
        
        if self.sell_in > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)
        self.setSell_in()



if __name__ == "__main__":

    
    item = RegularItem("NormalItem", 5, 10)
    print(item)

    for dia in range(1, 10):
        item.update_quality()
        print(item)