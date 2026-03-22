from .dish import Dish
from ..ingredients import Ingredient
import logging

class MeatDish(Dish):
    """
    Clase que representa un plato de carne.

    Hereda de la clase abstracta Dish y define el comportamiento
    específico para platos cuyos ingredientes deben ser de origen animal
    
    """
    def __init__(self, name, ingredients, servings):
        super().__init__(name, ingredients, servings, "CARNE")

    def is_vegan(self):
        return False
    
    def is_meat(self):
        for ingredient in self.ingredients:
            if ingredient.type != 'ANIMAL':
                return False
        return True
    
    def add_ingredient(self, ingredient: Ingredient):
        if ingredient.type != "ANIMAL":
            raise ValueError("Solo se pueden añadir ingredientes de origen animal")
        super().add_ingredient(ingredient)


        
    

