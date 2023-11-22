from lib.menu_items import MENU_ITEMS
from twilio.rest import Client
import datetime
import os

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
    

    def get_dish(self, dish_name):
        """Get an item from the menu and return the dish
        Params:
            dish_name - str representing the dish
        returns:
            dish object of dish name """
        for dish in self.dishes:
            if dish.name == dish_name:
                return dish
            
        return "Dish isn't on the menu"


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
            dish - dish object representing the dish
        Returns:
            nothing
        Side effects:
            adds menu item to the order. If menu item already in order
            then rather than add another it increased the amount varible
            in the dish object
        """
        if not hasattr(dish, 'name'):
            return None
        
        already_in = False
        for d in self.order:
            if d.name == dish.name:
                d.amount += 1
                self.total += d.price
                already_in = True

        if not already_in:
            self.order.append(dish)
            self.total += dish.price

    def remove_from_order(self, dish):
        """
        Params:
            dish - instance of dish to be removed from order
        Returns:
            nothing
        Side-effects:
            Removes dish from order list
        """
        index_to_pop = None
        for i in range(len(self.order)):
            # Remove the dish from the list if there is only one of them
            if self.order[i].name == dish.name and dish.amount == 1:
                index_to_pop = i
            # Or reduce the amount by 1 if there are multiple of same dish
            elif self.order[i].name == dish.name and dish.amount > 1:
                self.order[i].amount -= 1

        if index_to_pop is not None:
            self.order.pop(index_to_pop)


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
        receipt = '\n'.join([f"{dish.name}: (x{dish.amount}) £{dish.price*dish.amount:.2f}" for dish in self.order])
        receipt += '\n---------\n'
        return receipt + f"Total: £{self.total:.2f}"
    

    def checkout(self, customer_phone_no, timer=datetime):
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
        """
        if self.order == []:
            return "Nothing has been added to order"

        print("Thank you for your order")
        cur_time = timer.datetime.now()
        # est 30 mins for delivery
        plus30 = timer.timedelta(minutes=30)
        esttime = cur_time + plus30
        message_body = f"Thank you! Your order was placed. Total cost £{self.total:.2f}. Estimated delivery time: {esttime.hour}:{esttime.minute}"

        # Send a text if phone number is provided
        if customer_phone_no:
            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token  = os.environ['TWILIO_AUTH_TOKEN']
            sender_phone_no = os.environ['TWILIO_PHONE_NO']
            client = Client(account_sid, auth_token)

            client.messages.create(
                to=customer_phone_no,
                from_=sender_phone_no,
                body=message_body)

        return message_body


class Dish:
    def __init__(self, dish):
        """
        Creates a Dish instanst from dish (str)
        and sets price from MENU_ITEMS and sets amount
        to 1 at first
        """
        self.name = dish
        self.price = MENU_ITEMS[dish]
        self.amount = 1

    def add_one(self):
        self.amount += 1



