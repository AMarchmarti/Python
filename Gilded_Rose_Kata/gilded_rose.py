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
    cheese = AgedBrie("Cheese", 3, 0)

    magicwater = ConjuredItem ("Water", 5, 10)

    entrance = Backstage("Metalica", 2, 23)

    inventory = [cheese, magicwater, entrance]

    tienda = GildedRose(inventory)
    tienda.update_quality()

    assert cheese.getQuality() == 1
    assert entrance.getQuality() == 26
    assert magicwater.getQuality() == 8


    for i in range (1,10):
        tienda.update_quality()
    
    assert cheese.getQuality() == 17
    assert magicwater.getQuality() == 0
    assert entrance.getQuality() == 0