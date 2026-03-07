from .dish import Dish
from ingredients import Ingredient
import logging

class MeatDish(Dish):
    """
    Clase que define los meatdish
    """
    def __init__(self, name, ingredients, servings):
        super().__init(name, ingredients, servings, "CARNE")

    def is_vegan(self):
        return False
    
    def is_meat(self):
        for ingredient in self.ingredients:
            if ingredient.type != 'ANIMAL':
                return False
        return True
    
    def add_ingredient(self, ingredient: Ingredient):
        if ingredient.type != "ANIMAL":
            logging.info("Los ingredientes tienen que ser de origen animal")
            return False
        else:
            self.ingredients.append(ingredient)
            return True
        
    

