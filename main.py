from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee=CoffeeMaker()
money=MoneyMachine()
menu=Menu()

def whatToDo():
    choiceOption=['1', '2', '3', 'report', 'off']
    choose=None
    while not choose in choiceOption:
        choose=input('What would you like? (espresso(1)/latte(2)/cappuccino(3)):')
    return choose

def analyzing(choosenOption):
    activiteis={'report':CoffeeMaker.report(coffe)}
    return activiteis[choosenOption]



analyzing(whatToDo())