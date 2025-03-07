from item import Item
class IndianWine(Item):
    def update_quality(self):
        if self.quality < 50:
            self.quality += 1
            if self.sell_in < 0 and self.quality < 50:
                self.quality += 1
        self.sell_in -= 1