import pytest

from src.ollivanders import Ollivanders, Inventory, NormalItem, AgedBrie, Sulfuras, ConjuredItem, BackstagePass


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


# --- TESTS PARA CONJURED ITEMS ---

def test_conjured_item_degrades_double_speed():
    # Antes de caducar: baja 2 en lugar de 1
    item = ConjuredItem("Conjured Mana Cake", 10, 20)
    item.update_quality()
    assert item.sell_in == 9
    assert item.quality == 18

def test_conjured_item_degrades_double_speed_expired():
    # Caducado (sell_in <= 0): baja 4 en lugar de 2
    item = ConjuredItem("Conjured Mana Cake", 0, 20)
    item.update_quality()
    assert item.sell_in == -1
    assert item.quality == 16

def test_conjured_item_quality_never_negative():
    # No puede bajar de 0
    item = ConjuredItem("Conjured Mana Cake", 5, 1)
    item.update_quality()
    assert item.quality == 0


# --- TESTS PARA BACKSTAGE PASSES ---

def test_backstage_pass_increases_standard():
    # Más de 10 días: aumenta 1
    item = BackstagePass("Backstage passes", 15, 20)
    item.update_quality()
    assert item.quality == 21

def test_backstage_pass_increases_double():
    # 10 días o menos: aumenta 2
    item = BackstagePass("Backstage passes", 10, 20)
    item.update_quality()
    assert item.quality == 22

def test_backstage_pass_increases_triple():
    # 5 días o menos: aumenta 3
    item = BackstagePass("Backstage passes", 5, 20)
    item.update_quality()
    assert item.quality == 23

def test_backstage_pass_quality_drops_to_zero():
    # Día del concierto (sell_in 0) o después: calidad 0
    item = BackstagePass("Backstage passes", 0, 20)
    item.update_quality()
    assert item.quality == 0

def test_backstage_pass_max_quality():
    # No puede superar 50
    item = BackstagePass("Backstage passes", 5, 49)
    item.update_quality()
    assert item.quality == 50


# --- TEST DE INTEGRACIÓN (OLLIVANDERS) ---

def test_gilded_rose_add_item():
    shop = Ollivanders()

    normal = NormalItem("+5 Dexterity Vest", 10, 20)
    cheese = AgedBrie("Aged Brie", 2, 0)
    sulfuras = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)

    shop.add_item(normal)
    shop.add_item(cheese)
    shop.add_item(sulfuras)

    assert len(shop.inventory()) == 3

    items = [normal, cheese, sulfuras]
    assert shop.inventory() == items

    print("GildedRose addItem test:")
    print(shop)


def test_update_quality():
    shop = Ollivanders()

    normal = NormalItem("+5 Dexterity Vest", 10, 20)
    brie = AgedBrie("Aged Brie", 2, 0)

    shop.add_item(normal)
    shop.add_item(brie)

    assert len(shop.inventory()) == 2

    print("Dia 0:\n", shop)

    shop.update_date()

    assert shop.inventory()[0].quality == 19
    assert shop.inventory()[1].quality == 1

    print("Dia 1:\n", shop)



def test_ollivanders_full_update():
    shop = Ollivanders()
    items = [
        ConjuredItem("Conjured", 10, 20),
        BackstagePass("Pass", 11, 20),
        Sulfuras("Sulfuras", 0, 80)
    ]
    for item in items:
        shop.add_item(item)
    
    shop.update_date()
    
    # Conjured: 20 -> 18
    assert shop.inventory()[0].quality == 18
    # Backstage: 20 -> 22 (al actualizar, sell_in pasa de 11 a 10, entra en rango +2)
    assert shop.inventory()[1].quality == 22
    # Sulfuras: Fijo en 80
    assert shop.inventory()[2].quality == 80