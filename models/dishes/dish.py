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
        if not isinstance(ingredient, Ingredient):
            raise ValueError("Usa objetos ingrediente")
        
        for i in self.ingredients:
            if i.name == ingredient.name:
                raise ValueError("El alimento ya existe en el plato")
        
        else:
            self.ingredients.append(ingredient)


    def remove_ingredient(self, ingredient: Ingredient):
        if not isinstance(ingredient, Ingredient):
            raise ValueError("Usa objetos ingrediente")
        
        for i in self.ingredients:
            if ingredient.name == i.name:
                self.ingredients.remove(ingredient)
                return True
        else:
            return False
        
    def total_calories(self):
        for ingredient in self.ingredients:
            total += ingredient.total_calories()
        return total

    def calories_per_ingredient(self):
        calories = []
        for ingredient in self.ingredients:
            calories.append([ingredient.name, ingredient.total_calories()])
        return calories

    def contains_allergen(self, allergen: str):
        if not isinstance(allergen, str):
            raise ValueError()

        for i in range(len(self.ingredients)):
            for ingredient in self.ingredients:
                if ingredient.allergens[i] == allergen:
                    return True
        return False      
    
    def list_ingredients(self):
        return [ingredient.name for ingredient in self.ingredients]
    
    @abstractmethod
    def is_vegan(self):
        for ingredient in self.ingredients:
            if ingredient.type != ('PLANTA', 'MINERAL'):
                return False
        return True
    
    @abstractmethod
    def is_meat(self):
        for ingredient in self.ingredients:
            if ingredient.type != 'ANIMAL':
                return False
        return True
    
    def __str__(self):
        return f"Información del plato: \nNombre='{self.name}'\nTipo='{self.dish_type}' \n\
                Ingredientes: {self.list_ingredients()} \nCalorías totales={self.total_calories()}"