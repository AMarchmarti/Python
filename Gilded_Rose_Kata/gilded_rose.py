from regular_item import RegularItem
from agedbrie import AgedBrie
from conjured_item import ConjuredItem
from sulfuras import Sulfuras
from backstage import Backstage

class GildedRose(object):

    def __init__(self, items):
        self.items = items


    def update_quality(self):
        for item in self.items:
            item.update_quality()


if __name__ == "__main__":

    #Tests Cases
    Cheese = AgedBrie("Cheese", 3, 0)

    MagicWater = ConjuredItem ("Water", 5, 10)

    Entrance = Backstage("Metalica", 2, 23)

    inventory = [Cheese, MagicWater, Entrance]

    Tienda = GildedRose(inventory)
    Tienda.update_quality()

    assert Cheese.getQuality() == 1
    assert Entrance.getQuality() == 26
    assert MagicWater.getQuality() == 8


    for i in range (1,10):
        Tienda.update_quality()
    
    assert Cheese.getQuality() == 17
    assert MagicWater.getQuality() == 0
    assert Entrance.getQuality() == 0