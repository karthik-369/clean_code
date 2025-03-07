# -*- coding: utf-8 -*-

class HamaraBasket(object):

    def __init__(self, items):
        self.items = items

    


    def update_quality(self):
        def update_forest_honey(item):
            pass  
        def update_indian_wine(item):
            if item.quality < 50:
                item.quality += 1
                if item.sell_in < 0 and item.quality < 50:
                    item.quality += 1

        def update_movie_tickets(item):
            if item.sell_in > 0:
                item.quality += 1
                if item.sell_in < 11 and item.quality < 50:
                    item.quality += 1
                if item.sell_in < 6 and item.quality < 50:
                    item.quality += 1
            else:
                item.quality = 0  

        def update_regular_item(item):
            if item.quality > 0:
                item.quality -= 1
                if item.sell_in <= 0 and item.quality > 0:
                    item.quality -= 1  

        item_updaters = {
            'Forest Honey': update_forest_honey,
            'Indian Wine': update_indian_wine,
            'Movie Tickets': update_movie_tickets,
        }

        for item in self.items:
            item_updaters.get(item.name, update_regular_item)(item)
            if item.name != "Forest Honey":
                item.sell_in -= 1
    



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
