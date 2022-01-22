from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee=CoffeeMaker()
money=MoneyMachine()
menu=Menu()
on=True

def whatToDo():
    choiceOption=['1', '2', '3', 'report', 'off']
    choose=None
    while not choose in choiceOption:
        choose=input('What would you like? (espresso(1)/latte(2)/cappuccino(3)):')
    return choose


def analyzing(choosenOption):
    coffeeType={'1':'espresso', '2':'latte', '3':'cappuccino'}
    if choosenOption=='report':
        coffee.report()
    elif choosenOption=='off':
        escape()
    else:
        makeDrink(menu.find_drink(coffeeType[choosenOption]))


def escape():
    global on
    on=False

def makeDrink(typeOfCoffee):
    if coffee.is_resource_sufficient(typeOfCoffee):
        print('działa')


while on:
    analyzing(whatToDo())