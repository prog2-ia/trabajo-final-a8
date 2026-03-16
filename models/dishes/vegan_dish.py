from .dish import Dish
from ingredients import Ingredient

class VeganDish(Dish):
    """
    Clase que representa un plato vegano.

    Un plato vegano solo puede contener ingredientes de origen vegetal
    o mineral. Esta clase hereda de Dish y restringe los ingredientes
    permitidos para garantizar que el plato sea vegano
    
    """

    def __init__(self, name, ingredients, servings):
        super().__init__(name, ingredients, servings, "VEGANO")

    def is_vegan(self):
        for ingredient in self.ingredients:
            if ingredient.type not in ("PLANTA", "MINERAL"):
                return False
        return True

    def is_meat(self):
        return False

    def add_ingredient(self, ingredient: Ingredient):
        if ingredient.type not in ("PLANTA", "MINERAL"):
            raise ValueError("Solo se permiten alimentos de tipo planta o mineral")
        else:
            super().add_ingredient(ingredient) 

