import pytest

from src.ollivanders import Ollivanders, Inventory, NormalItem, AgedBrie, Sulfuras


def test_to_string():
    normal = NormalItem("+5 Dexterity Vest", 10, 20)
    print("toString() inheritance test")
    print(str(normal))


def test_update_quality_normal_item():
    normal = NormalItem("+5 Dexterity Vest", 10, 20)
    normal.update_quality()

    assert normal.name == "+5 Dexterity Vest"
    assert normal.sell_in == 9
    assert normal.quality == 19


def test_update_quality_normal_item_expired():
    normal = NormalItem("+5 Dexterity Vest", 0, 20)
    normal.update_quality()

    assert normal.sell_in == -1
    assert normal.quality == 18


def test_quality_normal_item_min_zero():
    normal = NormalItem("+5 Dexterity Vest", 10, 0)
    normal.update_quality()

    assert normal.sell_in == 9
    assert normal.quality == 0


def test_crear_aged_brie():
    cheese = AgedBrie("Aged Brie", 2, 0)

    assert cheese.name == "Aged Brie"
    assert cheese.sell_in == 2
    assert cheese.quality == 0


def test_update_quality_brie():
    cheese = AgedBrie("Aged Brie", 2, 0)
    cheese.update_quality()

    assert cheese.sell_in == 1
    assert cheese.quality == 1


#def test_gilded_rose_add_item():
#    shop = Ollivanders(Inventory([]))
#
#    normal = NormalItem("+5 Dexterity Vest", 10, 20)
#    cheese = AgedBrie("Aged Brie", 2, 0)
#    sulfuras = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)
#
#    shop.add_item(normal)
#    shop.add_item(cheese)
#    shop.add_item(sulfuras)
#
#    assert len(shop.inventory()) == 3
#
#    items = [normal, cheese, sulfuras]
#    assert shop.inventory() == items
#
#    print("GildedRose addItem test:")
#    print(shop)


#def test_update_quality():
#    shop = Ollivanders()
#
#    normal = NormalItem("+5 Dexterity Vest", 10, 20)
#    brie = AgedBrie("Aged Brie", 2, 0)
#
#    shop.add_item(normal)
#    shop.add_item(brie)
#
#    assert len(shop.inventory()) == 2
#
#    print("Dia 0:\n", shop)
#
#    shop.update_quality()
#
#    assert shop.inventory()[0].quality == 19
#    assert shop.inventory()[1].quality == 1
#
#    print("Dia 1:\n", shop)