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

def test_add_to_order_multiple_of_same_dish():
    # Commented lines running the test with multile
    # dish instances with the same values works the same
    order = Order()
    dish1 = Mock()
    # dish2 = Mock()
    # dish3 = Mock()
    dish1.name = 'Chicken Salad'
    # dish2.name = 'Chicken Salad'
    # dish3.name = 'Chicken Salad'
    dish1.price = 7
    # dish2.price = 7
    # dish3.price = 7
    dish1.amount = 1
    # dish2.amount = 1
    # dish3.amount = 1

    order.add_to_order(dish1)
    order.add_to_order(dish1)
    order.add_to_order(dish1)
    # order.add_to_order(dish2)
    # order.add_to_order(dish3)
    assert len(order.order) == 1
    assert order.order[0].amount == 3

def test_add_items_to_order_price_is_updated():
    order = Order()
    dish1 = Mock()
    dish2 = Mock()
    dish1.price = 4.55
    dish2.price = 2.20
    order.add_to_order(dish1)
    order.add_to_order(dish2)
    assert order.total == 6.75

"""Adding something other than a Dish object to the order
should do nothing and return none. Here we try just adding 
a plain str. It works with mock because the code just checks
if the object has a 'name' attribute"""
def test_add_to_order_with_something_other_than_dish_instance():
    order = Order()
    dish1 = Mock()
    dish2 = Mock()
    dish3 = 'hello'
    dish1.price = 4.55
    dish2.price = 2.20
    order.add_to_order(dish1)
    order.add_to_order(dish2)
    order_add = order.add_to_order(dish3)
    assert order.order == [dish1, dish2]
    assert order_add is None


def test_show_order():
    order = Order()
    dish1 = Mock()
    dish1.price = 4.55
    dish1.name = 'Pie'
    dish1.amount = 1
    dish2 = Mock()
    dish2.price = 2.20
    dish2.name = 'Peas'
    dish2.amount = 1
    order.add_to_order(dish1)
    order.add_to_order(dish2)
    assert order.show_order() == "Pie: (x1) £4.55\nPeas: (x1) £2.20\n---------\nTotal: £6.75"


def test_show_order_with_multiples_of_same_dish():
    order = Order()
    dish1 = Mock()
    dish2 = Mock()
    dish3 = Mock()
    dish4 = Mock()
    dish1.name = 'Chicken Salad'
    dish2.name = 'Chicken Salad'
    dish3.name = 'Chicken Salad'
    dish4.name = 'Pie'
    dish1.price = 7
    dish2.price = 7
    dish3.price = 7
    dish4.price = 2.5
    dish1.amount = 1
    dish2.amount = 1
    dish3.amount = 1
    dish4.amount = 1
    order.add_to_order(dish1)
    order.add_to_order(dish2)
    order.add_to_order(dish3)
    order.add_to_order(dish4)
    assert order.show_order() == 'Chicken Salad: (x3) £21.00\nPie: (x1) £2.50\n---------\nTotal: £23.50'


def test_check_out_with_no_dishes_in_order():
    order = Order()
    check_out = order.checkout("07123123123")
    assert check_out == "Nothing has been added to order"


# def test_correct_checkout_with_mock_time():
#     order = Order()
#     dish1 = Mock()
#     dish1.name = 'Chicken Salad'
#     dish1.price = 7
#     dish1.amount = 1
#     order.add_to_order(dish1)

#     time_mock = Mock()
#     time_mock.datetime.now.return_value = 15
#     time_mock.timedelta.return_value = 30
#     check_out = order.checkout("", timer=time_mock)
#     assert check_out == "Thank you! Your order was placed. Total cost £7.00. Estimated delivery time: 45"


def test_remove_from_order():
    order = Order()
    dish1 = Mock()
    dish2 = Mock()
    dish1.price = 4.55
    dish1.name = 'Pie'
    dish1.amount = 1
    dish2.price = 2.20
    dish2.name = 'Peas'
    dish2.amount = 1
    order.add_to_order(dish1)
    order.add_to_order(dish2)
    order.remove_from_order(dish1)
    assert order.order == [dish2]

def test_remove_dish_from_order_that_hasnt_been_added():
    order = Order()
    dish1 = Mock()
    dish2 = Mock()
    dish1.price = 4.55
    dish1.name = 'Pie'
    dish1.amount = 1
    dish2.price = 2.20
    dish2.name = 'Peas'
    dish2.amount = 1
    order.add_to_order(dish1)
    order.remove_from_order(dish2)
    assert order.order == [dish1]

def test_remove_dish_from_list_that_has_multiple_of_same_dish():
    order = Order()
    dish1 = Mock()
    dish1.name = 'Chicken Salad'
    dish1.price = 7
    dish1.amount = 1
    order.add_to_order(dish1)
    order.add_to_order(dish1)
    order.add_to_order(dish1)
    assert order.order[0].amount == 3

    order.remove_from_order(dish1)
    assert len(order.order) == 1
    assert order.order[0].amount == 2
