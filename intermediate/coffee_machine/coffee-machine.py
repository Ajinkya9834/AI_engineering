
# donePrompt user by asking “
# What would you like? (espresso/latte/cappuccino):​”

# doneTurn off the Coffee Machine by entering “
# off​” to the prompt. 

#done  Print report.
# Water: 100ml 
# Milk: 50ml 
# Coffee: 76g 
# # Money: $2.5

# Check resources sufficient? 

# Process coins.
#  Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01 
# Check transaction successful? 

# Make Coffee.

#Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If 
# latte was their choice of drink.

from menu import menu
from resources import resources

def current_ingredients_report(resources):
    print(f"Water: {resources["water"]} ml")
    print(f"CoCo: {resources["coco"]} g")
    print(f"Milk: {resources["milk"]} ml")

def print_cost_of_coffees():
    print(f"espresso: {menu["espresso"]["cost"]} $")
    print(f"latte: {menu["latte"]["cost"]} $")
    print(f"cappuccino: {menu["cappuccino"]["cost"]} $")

def process_coins(coffee_choice):
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    print("totla", total)
    if total > menu[coffee_choice]["cost"]:
        print(f"Your change: {total - menu[coffee_choice]["cost"]} $")
        total = total - menu[coffee_choice]["cost"]
        return total
    return total

def coffee_maker(coffee_choice):
    total_money = process_coins(coffee_choice)
    if total_money < menu[coffee_choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return
    
    for ingredient in menu[coffee_choice]["ingredients"]:
        if resources[ingredient] < menu[coffee_choice]["ingredients"][ingredient]:
            print(f"Sorry there resources")
            return
        
    for ingredient in menu[coffee_choice]["ingredients"]:
        resources[ingredient] -= menu[coffee_choice]["ingredients"][ingredient]
        
    print(f"Here is your {coffee_choice}. Enjoy!")
    


print_cost_of_coffees()

coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
print("coffee: ", coffee_choice)


if coffee_choice == "off off":
    print("shut down")
elif coffee_choice == "report":
    current_ingredients_report(resources)
elif coffee_choice == "espresso":
    coffee_maker(coffee_choice)
elif coffee_choice == "latte":
    coffee_maker(coffee_choice)
elif coffee_choice == "cappuccino":
    coffee_maker(coffee_choice)
