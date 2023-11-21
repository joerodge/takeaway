from lib.menu import Dish

def test_dish_is_created():
    dish = Dish('Kedgeree')
    assert dish.name == 'Kedgeree'
    assert dish.price == 8
    assert dish.amount == 1

def test_dish_add_one():
    dish = Dish('Kedgeree')
    dish.add_one()
    assert dish.amount == 2