from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee=CoffeeMaker()
money=MoneyMachine()
menu=Menu()
on = True

def whatToDo():
    choiceOption=['1', '2', '3', 'report', 'off']
    choose=None
    while not choose in choiceOption:
        choose=input(f'What would you like?:{menu.get_items()}\n1. $2.5\n2. $1.5\n3. $3\n')
    return choose


def analyzing(choosenOption):
    coffeeType={'1':'espresso', '2':'latte', '3':'cappuccino'}
    if choosenOption=='report':
        coffee.report()
        money.report()
    elif choosenOption=='off':
        escape()
    else:
        makeDrink(menu.find_drink(coffeeType[choosenOption]))


def escape():
    global on
    on=False

def makeDrink(typeOfCoffee):
    if coffee.is_resource_sufficient(typeOfCoffee):
        if money.make_payment(typeOfCoffee.cost):
            coffee.make_coffee(typeOfCoffee)

def machine():
    while on:
        analyzing(whatToDo())

machine()