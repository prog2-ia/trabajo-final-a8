from abc import ABC, abstractmethod 
from ingredients import Ingredient

class Dish(ABC):
    """
    Clase abstracta de la que heredan los tipos de platos
    """
    def __init__(self, name: str, ingredients: list[Ingredient], servings, dish_type):
        self.__name = name
        self.ingredients = ingredients
        self.servings = servings
        self.dish_type = dish_type

    @property
    def name(self):
        return self.__name
    
    @property
    def ingredients(self):
        return self.__ingredients
    
    @ingredients.setter
    def ingredients(self, value):
        if not isinstance(value, list):
            raise ValueError("Incluye los ingredientes usando una lista")
        
        for ingredient in value:
            if not isinstance(ingredient, Ingredient):
                raise ValueError("Utiliza objetos ingrediete")
            
        else:
            self.__ingredients = value

    @property
    def servings(self):
        return self.__servings
    
    @servings.setter
    def servings(self, value):
        if value <= 0:
            raise ValueError("El número de raciones ha de ser mayor que 0")
        else:
            self.__servings = value

    @property
    def dish_type(self):
        return self.__dish_type
    
    @dish_type.setter
    def dish_type(self, value):
        if value not in ("CARNE", "VEGANO", "MIXTO"):
            raise ValueError("Tipos de platos: 'CARNE', 'VEGANO', 'MIXTO")
        else:
            self.__dish_type = value

    # Métodos

    def add_ingredient(self, ingredient: Ingredient):
        pass
        