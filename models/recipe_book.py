"""
Código para gestionar recetarios de platos.

Define la estructura de un recetario con operaciones para
almacenar, filtrar y gestionar colecciones de platos.
"""


from models.dishes.dish import Dish


class RecipeBook:
    """
    Representa un recetario que almacena y gestiona platos.

    Attributes:
        name (str): Nombre del recetario
        dishes (list[Dish]): Lista de platos almacenados
    """
    def __init__(self, name: str) -> None:
        """
        Inicializa un recetario vacío con un nombre.
        """
        self.name = name
        self.dishes = []

    def add_dish(self, dish: Dish) -> None:
        """
        Añade un plato al recetario si no existe duplicado.

        Args:
            dish (Dish): Plato a añadir

        Raises:
            ValueError: Si el plato ya existe en el recetario
        """
        if dish in self.dishes:
            raise ValueError("El plato ya existe")
        self.dishes.append(dish)

    def remove_dish(self, dish: Dish) -> None:
        """
        Elimina un plato del recetario.

        Args:
            dish (Dish): Plato a eliminar

        Raises:
            ValueError: Si el plato no existe en el recetario
        """
        self.dishes.remove(dish)

    def filter_by_type(self, dish_type: str) -> list[Dish]:
        """
        Filtra platos por tipo (CARNE, VEGANO, MIXTO).

        Args:
            dish_type (str): Tipo de plato a filtrar

        Returns:
            list[Dish]: Lista de platos del tipo especificado
        """
        return [d for d in self.dishes if d.dish_type == dish_type]

    def filter_by_allergen(self, allergen: str) -> list[Dish]:
        """
        Obtiene platos que no contienen un alérgeno específico.

        Args:
            allergen (str): Alérgeno a evitar

        Returns:
            list[Dish]: Lista de platos seguros (sin el alérgeno)
        """
        return [d for d in self.dishes if not d.contains_allergen(allergen)]

    def __len__(self):
        return len(self.dishes)

    def __str__(self):
        return "\n".join([dish.name for dish in self.dishes])
