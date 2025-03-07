from h_basket import HamaraBasket
from regular_item import RegularItem
from item import Item
from movie_tickets import MovieTickets
from indian_wine import IndianWine
from forest_honey import ForestHoney
class DomainFactory:
    def single_item_provider(self, name: str, sell_in: int, quality: int):
        if name == "Regular Item":
            return [RegularItem(name, sell_in, quality)]
        elif name == 'Movie Tickets':
            return [MovieTickets(name, sell_in, quality)]
        elif name == 'Indian Wine':
            return [IndianWine(name, sell_in, quality)]
        elif name == 'Forest Honey':
            return [ForestHoney(name, sell_in, quality)]
        return [Item(name, sell_in, quality)]
        

    def update_quality(self, items):
        
        app = HamaraBasket(items)
        app.update_quality()