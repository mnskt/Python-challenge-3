from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

isRunning = True
user_money = 0

coffee_maker = CoffeeMaker()
menu = Menu()

while isRunning:
    user_drink_choice = str(input(f"What would you like? ({menu.get_items()}): "))
    if user_drink_choice == "off":
        print("Machine will be turned off.")
        isRunning = False
    if user_drink_choice == "report":
        coffee_maker.report()
    if user_drink_choice == "espresso" or user_drink_choice == "latte" or\
        user_drink_choice == "cappuccino":
        if coffee_maker.is_resource_sufficient(user_drink_choice):
