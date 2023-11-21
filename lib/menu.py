from lib.menu_items import MENU_ITEMS

class Menu:
    def __init__(self):
        """
        Sets a dictionary of menu items
        """
        pass

    def list_dishes(self):
        """
        Lists all dishes with price
        Params:
            None
        Returns:
            Formated str showing menu item and price separated
            by new line
            """
        pass


class Order:
    def __init__(self):
        """
        Sets order up to empty varible to empty dict
        and price to 0 and checkout time to None
        """
        self.order = {}
        self.total = 0

    def add_to_order(self, dish):
        """
        Adds a dish to the current order
        Params:
            dish - str representing the dish name
        Returns:
            nothing
        Side effects:
            adds menu item to the order
        """
        pass
        
    def show_order(self):
        """
        Shows itemised receipt of all items currently in
        order with total price
        Params:
            None
        Returns:
            formatted str with each item and price and a total
            at the end
        """
        pass

    def checkout(self, phone_no):
        """
        Finalise order and send text to customer with
        delivery time estimate
        Params:
            str - phone numer of customer to sent text to
        returns:
            None
        Side-effects:
            prints thank you for your order
            sends text to customer
            empties order variables
        """
        pass


class Dish:
    def __init__(self, dish):
        """Creates a Dish instanst from dish (str)
        and sets price from MENU_ITEMS and sets amount
        to 1 at first"""
        self.name = dish
        self.price = MENU_ITEMS[dish]
        self.amount = 1

    def add_one(self):
        self.amount += 1