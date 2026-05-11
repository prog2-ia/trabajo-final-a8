"""
Código para platos de tipo mixto.

Define la clase MixedDish que extiende Dish permitiendo cualquier
combinación de ingredientes de diferentes tipos (animal, vegetal, mineral).
"""


from .dish import Dish
from ..ingredients import Ingredient


class MixedDish(Dish):
    """
    Clase que representa un plato mixto.

    Un plato mixto puede contener ingredientes de distintos tipos
    (animal, vegetal o mineral). Esta clase hereda de Dish y define
    el comportamiento específico de este tipo de platos
    
    """

    def __init__(self, name: str, ingredients: list[Ingredient], servings: int) -> None:
        super().__init__(name, ingredients, servings, "MIXTO")

    def is_vegan(self) -> bool:
        """
        Verifica si el plato contiene al menos un ingrediente vegano.

        Returns:
            bool: True si contiene PLANTA o MINERAL, False si solo tiene ANIMAL
        """
        # un plato mixto es vegano si contiene al menos un ingrediente vegetal o mineral
        for ingredient in self.ingredients:
            if ingredient.type in ("PLANTA", "MINERAL"):
                return True
        return False
    
    def is_meat(self) -> bool:
        """
        Verifica si el plato contiene al menos un ingrediente animal.

        Returns:
            bool: True si contiene ANIMAL, False si solo tiene PLANTA/MINERAL
        """
        # un plato mixto contiene carne si tiene al menos un ingrediente animal
        for ingredient in self.ingredients:
            if ingredient.type == "ANIMAL":
                return True
        return False
    
    def add_ingredient(self, ingredient: Ingredient) -> str | None:
        """
        Añade un ingrediente al plato sin restricciones de tipo.

        Acepta cualquier tipo de ingrediente (ANIMAL, PLANTA, MINERAL).
        Si hay error (duplicado, etc.) lo retorna como string.

        Args:
            ingredient (Ingredient): Ingrediente a añadir

        Returns:
            str | None: Mensaje de error si falla, None si se añade correctamente
        """
        try:
            super().add_ingredient(ingredient)
        except ValueError as e:
            # capturar error y retornarlo como string en lugar de lanzar excepción
            return f"No se ha podido añadir al ingrediente al plato mixto. Error: {e}"
