from item import Item
class RegularItem(Item):
    def update_quality(self):
        print("called by item")
        if self.quality > 0:
            self.quality -= 1
            if self.sell_in <= 0 and self.quality > 0:
                self.quality -= 1
        self.sell_in -= 1