from datetime import date

class Updateable():
    
    def update_quality(self):
        pass

class Item(Updateable):

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = max(0, min(50, quality))


class Inventory:

    def __init__(self, items=None):
        self.items = items or []

    def update_all_items(self):
        for item in self.items:
            item.update_quality()

    def add_item(self, item):
        self.items.append(item)

class Ollivanders(Inventory):

    def __init__(self, items):
        Inventory.__init__(self, items)
        self.date = date.today()
    
    def update_date(self):
        self.update_all_items()
        self.date = date.today()

class NormalItem(Item):

    def update_quality(self):
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality = max(0, self.quality - 2)
        else:
            self.quality = max(0, self.quality - 1)

class AgedBrie(Item):

    def update_quality(self):
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality = min(50, self.quality + 2)
        else:
            self.quality = min(50, self.quality + 1)

class Sulfuras(Item):

    def update_quality(self):
        assert self.quality == 80, "Sulfuras es un item legendario y su calidad siempre debe ser 80"
        pass
