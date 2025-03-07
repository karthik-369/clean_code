from item import Item
class MovieTickets(Item):
    def update_quality(self):
        if self.sell_in > 0:
            if self.quality < 50:
                self.quality += 1
                if self.sell_in < 11 and self.quality < 50:
                    self.quality += 1
                if self.sell_in < 6 and self.quality < 50:
                    self.quality += 1
        else:
            self.quality = 0
        self.sell_in -= 1