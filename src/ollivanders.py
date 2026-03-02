from datetime import date

class Updateable():
    
    def update_quality(self):
        pass

class Item:

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Inventory():

    def __init__(self):
        self.items = []

    def update_all_items(self):
        for item in self.items:
            item.update_quality()

    def add_item(self, item):
        self.items.append(item)
    
    def getItems(self):
        return self.items

class Ollivanders(Inventory):

    def __init__(self):
        super().__init__()
        self.date = date.today()
    
    def update_date(self):from datetime import date

    def getItems(self):
        return self.inventory.getItems()



class NormalItem(Item, Updateable):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def setSell_in(self):
        self.sell_in -= 1

    def setQuality(self, value):
        if self.quality + value > 50:
            self.quality = 50
        elif self.quality + value >= 0:
            self.quality += value
        else:
            self.quality = 0

        if self.quality < 50:
            assert 0 <= self.quality <= 50, "La calidad de un item no puede ser negativa ni mayor a 50"

    def update_quality(self):

        if self.sell_in <= 0:
            self.setQuality(-2)
        else:
            self.setQuality(-1)
        self.setSell_in()


class AgedBrie(NormalItem):

    def __init__(self, name, sell_in, quality):
      NormalItem.__init__(self, name, sell_in, quality)


    def update_quality(self):

        if self.sell_in <= 0:
            self.setQuality(2)
        else:
            self.setQuality(1)

        self.setSell_in()



class BackstagePass(NormalItem):

    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def update_quality(self):

        if self.sell_in > 10:
            self.setQuality(1)
        elif self.sell_in > 5:
            self.setQuality(2)
        elif self.sell_in > 0:
            self.setQuality(3)
        else:
            self.quality = 0
        
        self.setSell_in()

            
        
class ConjuredItem(NormalItem):

    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def update_quality(self):

        if self.sell_in <= 0:
            self.setQuality(-4)
        else:
            self.setQuality(-2)

        self.setSell_in()


class Sulfuras(NormalItem):

    def setQuality(self):
        self.quality = 80
        assert self.quality == 80, "Sulfuras es un item legendario y su calidad siempre debe ser 80"

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