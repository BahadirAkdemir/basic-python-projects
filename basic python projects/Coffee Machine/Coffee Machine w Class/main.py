from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
manu = Menu()
money_machine = MoneyMachine()
while True:
    print(manu.get_items())
    machine.report()
    print("What would you like to order?")
    order = input()
    item = manu.find_drink(order)
    if item:
        if machine.is_resource_sufficient(item):
            if money_machine.make_payment(item.cost):
                machine.make_coffee(item)
    money_machine.report()
