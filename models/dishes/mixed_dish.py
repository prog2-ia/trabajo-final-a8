from .dish import Dish
from ingredients import Ingredient

class MixedDish(Dish):
    """
    Clase que representa un plato mixto.

    Un plato mixto puede contener ingredientes de distintos tipos
    (animal, vegetal o mineral). Esta clase hereda de Dish y define
    el comportamiento específico de este tipo de platos
    
    """

    def __init__(self, name, ingredients, servings):
        super().__init__(name, ingredients, servings, "MIXTO")

    def is_vegan(self):
        for ingredient in self.ingredients:
            if ingredient.type in ("PLANTA", "MINERAL"):
                return True
        return False
    
    def is_meat(self):
        for ingredient in self.ingredients:
            if ingredient.type == "ANIMAL":
                return True
        return False
    
    def add_ingredient(self, ingredient: Ingredient):
        try:
            super().add_ingredient(ingredient)
        except ValueError as e:
            return f"No se ha podido añadir al ingrediente al plato mixto \
                    Error: {e}"