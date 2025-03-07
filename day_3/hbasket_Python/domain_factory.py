from h_basket import Item, HamaraBasket

class DomainFactory:
    def single_item_provider(self, name: str, sell_in: int, quality: int):
        return [Item(name=name, sell_in=sell_in, quality=quality)]

    def update_quality(self, items):
        app = HamaraBasket(items)
        app.update_quality()
