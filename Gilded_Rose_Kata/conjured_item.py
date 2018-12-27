from item import Item
class ConjuredItem(Item):

    def update_quality(self):

        if self.sell_in > 0:
            self.setQuality(-2)
        else:
            self.setQuality(-4)
        self.setSell_in()

if __name__ == "__main__":

    
    item = ConjuredItem("Elixir of mongoose", 5, 20)
    print(item)

    for dia in range(1, 10):
        item.update_quality()
        print(item)