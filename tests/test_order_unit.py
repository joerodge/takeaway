from lib.menu import Order
from unittest.mock import Mock

def test_empty_order_created_at_first():
    order = Order()
    assert order.order ==[]
    assert order.total == 0

def test_add_items_to_order():
    order = Order()
    dish1 = Mock()
    dish2 = Mock()
    dish1.price = 4.55
    dish2.price = 2.20
    order.add_to_order(dish1)
    order.add_to_order(dish2)
    assert order.order == [dish1, dish2]

def test_add_items_to_order_price_is_updated():
    order = Order()
    dish1 = Mock()
    dish2 = Mock()
    dish1.price = 4.55
    dish2.price = 2.20
    order.add_to_order(dish1)
    order.add_to_order(dish2)
    assert order.total == 6.75

def test_show_order_with_one_item():
    order = Order()
    dish1 = Mock()
    dish1.price = 4.55
    dish1.name = 'Pie'
    dish2 = Mock()
    dish2.price = 2.20
    dish2.name = 'Peas'
    order.add_to_order(dish1)
    order.add_to_order(dish2)
    assert order.show_order() == "Pie: £4.55\nPeas: £2.20\n---------\nTotal: £6.75"