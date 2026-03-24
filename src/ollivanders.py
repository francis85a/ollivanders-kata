from datetime import date, timedelta

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"

class Inventory:
    def __init__(self):
        self.items = []

    def update_all_items(self):
        for item in self.items:
            item.update_quality()

    def add_item(self, item):
        self.items.append(item)
    
    def inventory(self):
        return self.items

class Ollivanders(Inventory):
    def __init__(self):
        super().__init__()
        self.today = date.today()
    
    def update_date(self):
        self.today += timedelta(days=1)
        self.update_all_items()

class NormalItem(Item):
    def setQuality(self, value):
        self.quality += value
        if self.quality > 50: self.quality = 50
        if self.quality < 0: self.quality = 0

    def update_quality(self):
        self.sell_in -= 1
        if self.sell_in < 0:
            self.setQuality(-2)
        else:
            self.setQuality(-1)

class AgedBrie(NormalItem):
    def update_quality(self):
        self.sell_in -= 1
        if self.sell_in < 0:
            self.setQuality(2)
        else:
            self.setQuality(1)

class BackstagePass(NormalItem):
    def update_quality(self):
        # Primero restamos el día
        self.sell_in -= 1
        
        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in <= 5:
            self.setQuality(3)
        elif self.sell_in <= 10:
            self.setQuality(2)
        else:
            self.setQuality(1)

class ConjuredItem(NormalItem):
    def update_quality(self):
        self.sell_in -= 1
        if self.sell_in < 0:
            self.setQuality(-4)
        else:
            self.setQuality(-2)

class Sulfuras(Item):
    def __init__(self, name, sell_in, quality):
        # Sulfuras es siempre 80 y no hereda límites de NormalItem
        super().__init__(name, 0, 80)

    def update_quality(self):
        pass
    
def main():
    shop = Ollivanders()
    normal = NormalItem("+5 Dexterity Vest", 10, 20)
    cheese = AgedBrie("Aged Brie", 2, 0)
    sulfuras = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
    conjured = ConjuredItem("Conjured", 10, 20)
    backstage = BackstagePass("Backstage Pass", 11, 20)

    shop.add_item(normal)
    shop.add_item(cheese)
    shop.add_item(sulfuras)
    shop.add_item(conjured)
    shop.add_item(backstage)
    shop.update_date()
    shop.update_all_items()

    print ("Dia 1:\n", normal)
if __name__ == "__main__":
    main()