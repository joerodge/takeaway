from lib.menu import *


def test_get_dish_from_menu_returns_correct_dish_object():
    menu = Menu()
    dish = menu.get_dish('Avocado on Toast')
    assert dish.name == 'Avocado on Toast'
    assert dish.price == 7.5

def test_get_dish_not_on_menu():
    menu = Menu()
    dish = menu.get_dish('Salmon')
    assert dish == "Dish isn't on the menu"


def test_get_item_from_menu_and_add_to_order():
    menu = Menu()
    dish1 = menu.get_dish('Avocado on Toast')
    dish2 = menu.get_dish('Kedgeree')
    order = Order()
    order.add_to_order(dish1)
    order.add_to_order(dish2)
    assert order.order == [dish1, dish2]

def test_get_multiple_of_same_dish_from_menu_and_add_to_order():
    menu = Menu()
    dish1 = menu.get_dish('Avocado on Toast')
    dish2 = menu.get_dish('Avocado on Toast')
    order = Order()
    order.add_to_order(dish1)
    order.add_to_order(dish2)
    assert order.order == [dish1]
    assert order.order[0].amount == 2


def test_correct_check_out():
    menu = Menu()
    dish1 = menu.get_dish('Avocado on Toast')
    dish2 = menu.get_dish('Kedgeree')
    order = Order()
    order.add_to_order(dish1)
    order.add_to_order(dish2)
    check_out = order.checkout('')
    assert check_out.startswith("Thank you! Your order was placed")


