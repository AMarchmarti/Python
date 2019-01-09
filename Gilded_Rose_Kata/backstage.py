from regular_item import RegularItem
class Backstage(RegularItem):

    def update_quality(self):

        if self.sell_in > 10:
            self.setQuality(1)

        elif self.sell_in > 5 :
            self.setQuality(2)

        elif self.sell_in > 0:
            self.setQuality(3)
        else:
            self.quality = 0

        self.setSell_in()


if __name__ == '__main__':

    # Correct Test Case
    item = Backstage("Backstage", 0, 0)
    print(item)

    for dia in range(0, 10):
        item.update_quality()
        print(item)
    
    # Incorrect Test Case
    item = Backstage("Backstage", 2, 100)
    for dia in range(1, 10):
        item.update_quality()
        print(item)