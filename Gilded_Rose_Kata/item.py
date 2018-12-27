from interface_updatable import Updatable
class Item(Updatable):

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

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


    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


if __name__ == "__main__":

    
    item = Item("NormalItem", 5, 10)
    print(item)

    for dia in range(1, 10):
        item.update_quality()
        print(item)