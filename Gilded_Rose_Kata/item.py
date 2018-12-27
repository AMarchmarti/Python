class Item():

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


    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)