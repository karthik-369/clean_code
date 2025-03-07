class Item:
    def __init__(self, name: str, sell_in: int, quality: int):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"


class HamaraBasket:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Forest Honey":
                continue  # Forest Honey does not change

            if item.name == "Indian Wine":
                self.increase_quality(item)
            elif item.name == "Movie Tickets":
                if item.sell_in > 10:
                    self.increase_quality(item)
                elif item.sell_in > 5:
                    self.increase_quality(item, 2)  # Increase by 2 when 10 days or less
                elif item.sell_in > 0:
                    self.increase_quality(item, 3)  # Increase by 3 when 5 days or less
                else:
                    item.quality = 0  # Quality drops to 0 after the concert
            else:
                self.decrease_quality(item)

            # Reduce SellIn for all items except Forest Honey
            item.sell_in -= 1

            # If SellIn < 0, regular items degrade twice as fast
            if item.sell_in < 0:
                if item.name == "Indian Wine":
                    self.increase_quality(item)
                elif item.name != "Movie Tickets":
                    self.decrease_quality(item)

    def increase_quality(self, item, amount=1):
        item.quality = min(50, item.quality + amount)

    def decrease_quality(self, item, amount=1):
        item.quality = max(0, item.quality - amount)


class DomainFactory:
    def single_item_provider(self, name: str, sell_in: int, quality: int):
        return [Item(name, sell_in, quality)]

    def update_quality(self, items):
        app = HamaraBasket(items)
        app.update_quality()
