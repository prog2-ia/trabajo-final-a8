from .dish import Dish
from ingredients import Ingredient

class MixedDish(Dish):
    """
    Clase que define los platos combinados
    """

    def __init__(self, name, ingredients, servings):
        super().__init__(name, ingredients, servings, "MIXTO")

    def is_vegan(self):
        for ingredient in self.ingredients:
            if ingredient.type not in ("PLANTA", "MINERAL"):
                return False
        return True
    
    def is_meat(self):
        for ingredient in self.ingredients:
            if ingredient.type != "ANIMAL":
                return False
        return True
    
    def add_ingredient(self, ingredient: Ingredient):
        try:
            super().add_ingredient(ingredient)
        except ValueError as e:
            return f"No se ha podido añadir al ingrediente al plato mixto \
                    Error: {e}"