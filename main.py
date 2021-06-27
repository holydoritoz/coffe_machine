from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


items = Menu() ## Method, Get_items, find_drink(order_name)
money_system = MoneyMachine() ## report(), make_payment(cost)
coffee_maker = CoffeeMaker() ## report(), is_resouce_sufficiente(drink), make_coffee(order)

is_on = True


while is_on:
    options = items.get_items()
    choice = input(f'What would you like? {options}: ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_system.report()
    else:
        drink = items.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_system.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
