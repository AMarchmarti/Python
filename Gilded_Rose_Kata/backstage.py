from item import Item
class Backstage(Item):

    def setQuality(self, valor):
        if self.quality + valor <= 50:
            self.quality = self.quality + valor
        else:
            self.quality
    
        assert 0 <= self.quality <= 50, "quality de %s fuera de rango" % self.__class__.__name__

    def update_quality(self):

        if self.sell_in > 10:
            self.setQuality(1)

        elif self.sell_in > 5 :
            self.setQuality(2)

        elif self.sell_in <= 5:
            self.setQuality(3)

        self.setSell_in()


if __name__ == '__main__':

    # Correct Test Case
    item = Backstage("Backstage", 9, 0)
    print(item)

    for dia in range(0, 10):
        item.update_quality()
        print(item)
    
    # Incorrect Test Case
    item = Backstage("Backstage", 2, 100)
    for dia in range(1, 10):
        item.update_quality()
        print(item)