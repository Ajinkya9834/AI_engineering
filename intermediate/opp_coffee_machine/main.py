from menu import Menu, MenuItem
from coffee_macker import CoffeeMaker
from money_machine import MoneyMachine

# definations

def make_coffee(drink, coffeeMaker_obj, moneyMachine_obj):
    if coffeeMaker_obj.is_resource_sufficient(drink) and moneyMachine_obj.make_payment(drink.cost):
            coffeeMaker_obj.make_coffee(drink)

# main code
menu_obj = Menu()
coffeeMaker_obj = CoffeeMaker()
moneyMachine_obj = MoneyMachine()

while True:
    order_name = input(f"What would you like? {menu_obj.get_items()}:")
    print(order_name)

    if order_name == "latte" or order_name == "espresso" or order_name == "cappuccino":
        drink = menu_obj.find_drink(order_name)
        make_coffee(drink, coffeeMaker_obj, moneyMachine_obj)
    elif order_name == "report":
        coffeeMaker_obj.report()
        moneyMachine_obj.report()
    elif order_name == "off":
        print("shut down")
        break
    else:
        print("invalid choice")