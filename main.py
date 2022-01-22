from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def whatToDo():
    choiceOption=['1', '2', '3', 'report', 'off']
    while not choose in choiceOption:
        choose=input('What would you like? (espresso(1)/latte(2)/cappuccino(3)):')
    return choose

def analyzing(choosenOption):



analyzing(whatToDo())