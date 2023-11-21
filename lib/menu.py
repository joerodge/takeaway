from lib.menu_items import MENU_ITEMS

class Menu:
    def __init__(self):
        """
        Sets a list of dish objects from all items on menu
        """
        self.dishes =[]
        for dish_name in MENU_ITEMS:
            dish = Dish(dish_name)
            self.dishes.append(dish)

    def list_dishes(self):
        """
        Lists all dishes with price
        Params:
            None
        Returns:
            Formated str showing menu item and price separated
            by new line
            """
        return '\n'.join([f"{dish.name}: £{dish.price:.2f}" for dish in self.dishes])


class Order:
    def __init__(self):
        """
        Sets order up to empty order list and price to 0
        """
        self.order = []
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
        self.order.append(dish)
        self.total += dish.price

        
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
        receipt = '\n'.join([f"{dish.name}: £{dish.price:.2f}" for dish in self.order])
        receipt += '\n---------\n'
        return receipt + f"Total: £{self.total:.2f}"
    

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