"""
Código para gestionar menús semanales.

Define la estructura de un menú semanal con operaciones para
comparar, agregar ingredientes y calcular calorías.
"""


from models.dishes.dish import Dish


class WeeklyMenu:
    """
    Representa un menú semanal asignando un plato a cada día.

    Attributes:
        menu (dict[str, Dish]): Diccionario que mapea días a platos
    """
    def __init__(self) -> None:
        """
        Inicializa un menú vacío.
        """
        self.menu = {}

    def add_day(self, day: str, dish: Dish) -> None:
        """
        Asigna un plato a un día específico.

        Args:
            day (str): Nombre del día
            dish (Dish): Plato a asignar
        """
        self.menu[day] = dish

    def total_calories(self) -> float:
        """
        Calcula el total de calorías del menú semanal.

        Returns:
            float: Suma de calorías de todos los platos
        """
        return sum(dish.total_calories() for dish in self.menu.values())

    def __add__(self, other: "WeeklyMenu") -> dict[str, float]:
        """
        Genera una lista de compra combinando ingredientes de dos menús.
        """
        shopping_list = {}

        # iterar sobre ambos menús para recopilar todos los ingredientes
        for menu in [self, other]:
            for dish in menu.menu.values():
                for ing in dish.ingredients:
                    # acumular cantidades si el ingrediente ya existe
                    if ing.name in shopping_list:
                        shopping_list[ing.name] += ing.quantity
                    else:
                        shopping_list[ing.name] = ing.quantity

        return shopping_list

    def __gt__(self, other: "WeeklyMenu") -> bool:
        """
        Compara si este menú tiene más calorías que otro.
        """
        return self.total_calories() > other.total_calories()

    def __lt__(self, other: "WeeklyMenu") -> bool:
        """
        Compara si este menú tiene menos calorías que otro.
        """
        return self.total_calories() < other.total_calories()

    def __getitem__(self, day: str) -> Dish:
        """
        Obtiene el plato asignado a un día específico.
        """
        return self.menu[day]

    def __str__(self) -> str:
        return "\n".join([f"{day}: {dish.name}" for day, dish in self.menu.items()])
