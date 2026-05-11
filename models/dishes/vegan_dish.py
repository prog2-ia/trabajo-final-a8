"""
Código para platos de tipo vegano.

Define la clase VeganDish que extiende Dish con restricciones
para garantizar que solo contiene ingredientes vegetales o minerales.
"""


from .dish import Dish
from ..ingredients import Ingredient
from exceptions.custom_exceptions import IncompatibleIngredientError


class VeganDish(Dish):
    """
    Clase que representa un plato vegano.

    Un plato vegano solo puede contener ingredientes de origen vegetal
    o mineral. Esta clase hereda de Dish y restringe los ingredientes
    permitidos para garantizar que el plato sea vegano
    
    """

    def __init__(self, name: str, ingredients: list[Ingredient], servings: int) -> None:
        super().__init__(name, ingredients, servings, "VEGANO")

    def is_vegan(self) -> bool:
        """
        Verifica si el plato es realmente vegano (solo PLANTA o MINERAL).

        Returns:
            bool: True si todos los ingredientes son veganos, False en caso contrario
        """
        # verificar que todos los ingredientes sean de tipo PLANTA o MINERAL
        for ingredient in self.ingredients:
            if ingredient.type not in ("PLANTA", "MINERAL"):
                return False
        return True

    def is_meat(self) -> bool:
        """
        Verifica si el plato contiene carne.

        Returns:
            bool: Siempre False, los platos veganos nunca contienen carne
        """
        return False

    def add_ingredient(self, ingredient: Ingredient) -> None:
        """
        Añade un ingrediente al plato si es vegano (PLANTA o MINERAL).

        Args:
            ingredient (Ingredient): Ingrediente a añadir

        Raises:
            IncompatibleIngredientError: Si el ingrediente no es de tipo PLANTA o MINERAL
        """
        # validar que el ingrediente sea compatible con platos veganos
        if ingredient.type not in ("PLANTA", "MINERAL"):
            raise IncompatibleIngredientError("Solo se permiten alimentos de tipo planta o mineral")
        else:
            super().add_ingredient(ingredient) 

