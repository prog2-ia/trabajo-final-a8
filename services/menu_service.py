import random
from models.weekly_menu import WeeklyMenu


def generate_weekly_menu(dishes):
    menu = WeeklyMenu()
    days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for day in days:
        menu.add_day(day, random.choice(dishes))

    return menu


def print_menu(menu):
    for day, dish in menu.items():
        print(f"{day}: {dish.name}")