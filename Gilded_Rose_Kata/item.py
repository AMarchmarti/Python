
class Item:

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def getName(self):
        return self.name

    def getSell_in(self):
        return self.sell_in
    
    def getQuality(self):
        return self.quality

    


    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


