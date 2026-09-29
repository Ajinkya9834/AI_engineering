from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

order_name = input("What would you like? (espresso/latte/cappuccino):")
print(order_name)

menuItem_obj = MenuItem(name = order_name, water = 100, milk = 0, coffee = 16, cost = 1.5)
menu_obj = Menu()

coffeeMaker_obj = CoffeeMaker()
moneyMachine_obj = MoneyMachine()


if order_name == "latte":
    enough_resources = coffeeMaker_obj.is_resource_sufficient(menuItem_obj)
    if enough_resources:
        # money_received = 
        payment_successful = moneyMachine_obj.make_payment(menuItem_obj.cost)
        if(payment_successful):
            coffeeMaker_obj.make_coffee(menuItem_obj)
    make_coffee(menuItem_obj, coffeeMaker_obj, moneyMachine_obj)
elif order_name == "espresso":
    canmake = coffeeMaker_obj.is_resource_sufficient(order_name)
    make_coffee(menuItem_obj, coffeeMaker_obj, moneyMachine_obj)
elif order_name == "cappuccino":
    canmake = coffeeMaker_obj.is_resource_sufficient(order_name)
elif order_name == "report":
    coffeeMaker_obj.report()
    moneyMachine_obj.report()
elif order_name == "off":
    print("shut down")


