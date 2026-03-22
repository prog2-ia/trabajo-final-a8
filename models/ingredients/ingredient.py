from abc import ABC, abstractmethod 
from exceptions.custom_exceptions import InvalidUnitError


class Ingredient(ABC):
    """
    Clase abstracta que representa un ingrediente.

    Define las propiedades y comportamientos comunes que deben tener
    todos los ingredientes utilizados en los platos.

    Attributes
    ----------
    _name : str
        Nombre del ingrediente.
    __quantity : float
        Cantidad del ingrediente en gramos.
    __calories_per_100g : float
        Número de calorías por cada 100 gramos.
    __type : str
        Tipo de ingrediente ("ANIMAL", "PLANTA" o "MINERAL").
    __allergens : list[str]
        Lista de alérgenos que contiene el ingrediente.
    """

    def __init__(self, name: str, quantity: float, calories_per_100g: float, type: str, allergens: list[str]):
        self._name = name
        self.quantity = quantity
        self.calories_per_100g = calories_per_100g
        self.type = type
        self.allergens = allergens

    @property
    def name(self):
        return self._name
    
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise InvalidUnitError("Cantidad ha de ser mayor a 1 gramo")
        else:
            self.__quantity = value
        
    @property
    def calories_per_100g(self):
        return self.__calories_per_100g
    
    @calories_per_100g.setter
    def calories_per_100g(self, value):
        if value < 0:
            raise ValueError("EL número de calorías ha de ser mayor que 0")
        else:
            self.__calories_per_100g = value

    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, value):
        if value not in ("ANIMAL", "PLANTA", "MINERAL"):
            raise ValueError("Tipo de alimento no disponible")
        else:
            self.__type = value

    @property
    def allergens(self):
        return self.__allergens
    
    @allergens.setter
    def allergens(self, value):
        if not isinstance(value, list):
            raise ValueError("Hay que pasar los alérgenos empleando una lista")

        for allergen in value:
            if not isinstance(allergen, str):
                raise ValueError("No introduzca números porfavor")
        else:
            self.__allergens = value

    def total_calories(self):
        return (self.calories_per_100g * self.quantity) /100
    
    def is_allergen(self, allergen: str):
        if not isinstance(allergen, str):
            raise ValueError("Introduzca el alérgeno con letras porfavor")
        else:
            return allergen in self.allergens
    
    def __str__(self):
        return f"Información alimento: Ingredient[name='{self.name}',\
                quantity={self.quantity}, calories_per_100g={self.calories_per_100g},\
                allergens={self.allergens}]"
