"""
Código para gestionar menús semanales.

Proporciona funcionalidades para generar y mostrar menús semanales.
"""


import random
from models.dishes.dish import Dish
from models.weekly_menu import WeeklyMenu


def generate_weekly_menu(dishes: list[Dish]) -> WeeklyMenu:
    """
    Genera un menú semanal asignando aleatoriamente un plato a cada día.

    Args:
        dishes (list[Dish]): Lista de platos disponibles

    Returns:
        WeeklyMenu: Menú semanal con platos seleccionados aleatoriamente

    Raises:
        IndexError: Si la lista de platos está vacía
    """
    menu = WeeklyMenu()
    days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    # asignar un plato aleatorio a cada día de la semana
    for day in days:
        menu.add_day(day, random.choice(dishes))

    return menu


def print_menu(menu: WeeklyMenu) -> None:
    """
    Muestra el menú semanal en formato legible.

    Args:
        menu (WeeklyMenu): Menú semanal a mostrar
    """
    for day, dish in menu.items():
        print(f"{day}: {dish.name}")
