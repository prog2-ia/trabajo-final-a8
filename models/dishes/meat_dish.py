"""
Código para platos de tipo carne.

Define la clase MeatDish que extiende Dish con restricciones
para garantizar que solo contiene ingredientes de origen animal.
"""


from .dish import Dish
from ..ingredients import Ingredient
from exceptions.custom_exceptions import IncompatibleIngredientError


class MeatDish(Dish):
    """
    Clase que representa un plato de carne.

    Hereda de la clase abstracta Dish y define el comportamiento
    específico para platos cuyos ingredientes deben ser de origen animal
    
    """
    def __init__(self, name: str, ingredients: list[Ingredient], servings: int) -> None:
        super().__init__(name, ingredients, servings, "CARNE")

    def is_vegan(self) -> bool:
        """
        Verifica si el plato es vegano.

        Returns:
            bool: Siempre False, los platos de carne nunca son veganos
        """
        return False
    
    def is_meat(self) -> bool:
        """
        Verifica si el plato es de carne.

        Returns:
            bool: True si todos los ingredientes son de origen animal, False en caso contrario
        """
        # verificar que todos los ingredientes sean de tipo animal
        for ingredient in self.ingredients:
            if ingredient.type != 'ANIMAL':
                return False
        return True
    
    def add_ingredient(self, ingredient: Ingredient) -> None:
        """
        Añade un ingrediente al plato si es de origen animal.

        Args:
            ingredient (Ingredient): Ingrediente a añadir

        Raises:
            IncompatibleIngredientError: Si el ingrediente no es de tipo ANIMAL
        """
        # validar que el ingrediente sea de origen animal
        if ingredient.type != "ANIMAL":
            raise IncompatibleIngredientError("Solo se pueden añadir ingredientes de origen animal")
        super().add_ingredient(ingredient)
