# -*- coding: utf-8 -*-

class HamaraBasket(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == 'Forest Honey':
                continue 
            if item.name == "Indian Wine":
                if item.quality < 50:
                    item.quality += 1
                    if item.sell_in < 0 and item.quality < 50:
                        item.quality += 1
            elif item.name == "Movie Tickets":
                if item.sell_in > 0:
                    item.quality += 1
                    if item.sell_in < 11 and item.quality < 50:
                        item.quality += 1
                    if item.sell_in < 6 and item.quality < 50:
                        item.quality += 1
                else:
                    item.quality = 0  # Quality drops to 0 after the event
            else:  # Regular items
                if item.quality > 0:
                    item.quality -= 1
                    if item.sell_in < 0 and item.quality > 0:
                        item.quality -= 1  # Degrades twice as fast after sell-in
            item.sell_in -= 1
    



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
