class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"

    def update_quality(self):
        pass