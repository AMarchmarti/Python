from item import Item
class Sulfuras(Item):

    def setSell_in(self):
        pass

    def update_quality(self):
        assert self.quality == 80, "Quality de %s no es 80" % self.__class__.__name__
        self.quality = 80



if __name__ == '__main__':

    item = Sulfuras("Sulfuras, mano de Maradona", 3, 80)
    print(item)
    # test update_quality
    for dia in range(1, 10):
        item.update_quality()
        print(item)

    # test update_quality incorret input
    item = Sulfuras("Sulfuras, mano de Dios", 3, 10000)
    for dia in range(1, 10):
        item.update_quality()
        print(item)