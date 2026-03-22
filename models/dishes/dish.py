from abc import ABC, abstractmethod
from ..ingredients import Ingredient
from exceptions.custom_exceptions import InvalidServingError

class Dish(ABC):
    """
    Clase abstracta que representa un plato.

    Esta clase define la estructura común que tendrán todos los tipos de platos
    del sistema. No debe instanciarse directamente, sino que debe heredarse
    para crear tipos concretos de platos (por ejemplo, platos veganos o de carne).

    Attributes
    ----------
    _name : str
        Nombre del plato.
    __ingredients : list[Ingredient]
        Lista de ingredientes que componen el plato.
    __servings : int
        Número de raciones del plato.
    __dish_type : str
        Tipo de plato. Puede ser "CARNE", "VEGANO" o "MIXTO".
    """

    def __init__(self, name: str, ingredients: list[Ingredient], servings, dish_type):
        self._name = name
        self.ingredients = ingredients
        self.servings = servings
        self.dish_type = dish_type

    @property
    def name(self):
        return self._name
    
    @property
    def ingredients(self):
        return self.__ingredients
    
    @ingredients.setter
    def ingredients(self, value):
        if not isinstance(value, list):
            raise ValueError("Incluye los ingredientes usando una lista")
        for ingredient in value:
            if not isinstance(ingredient, Ingredient):
                raise ValueError("Utiliza objetos ingrediente")
        else:
            self.__ingredients = value

    @property
    def servings(self):
        return self.__servings
    
    @servings.setter
    def servings(self, value):
        if value <= 0:
            raise InvalidServingError("El número de raciones ha de ser mayor que 0")
        else:
            self.__servings = value

    @property
    def dish_type(self):
        return self.__dish_type
    
    @dish_type.setter
    def dish_type(self, value):
        if value not in ("CARNE", "VEGANO", "MIXTO"):
            raise ValueError("Tipos de platos: 'CARNE', 'VEGANO', 'MIXTO'")
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
            if i.name == ingredient.name:
                self.ingredients.remove(i)
                return True
        return False
        
    def total_calories(self):
        total = 0
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
            raise ValueError("El alérgeno debe ser un string")
        for ingredient in self.ingredients:
            if ingredient.is_allergen(allergen):
                return True
        return False      
    
    def list_ingredients(self):
        return [ingredient.name for ingredient in self.ingredients]
    
    @abstractmethod
    def is_vegan(self):
        """
        Este método se implementa en subclases
        """
        pass

    @abstractmethod
    def is_meat(self):
        """
        Este método se implementa en subclases
        """
        pass
    
    def __str__(self):
        return (f"Información del plato: \n"
                f"Nombre='{self.name}'\n"
                f"Tipo='{self.dish_type}' \n"
                f"Ingredientes: {self.list_ingredients()} \n"
                f"Calorías totales={self.total_calories()}")