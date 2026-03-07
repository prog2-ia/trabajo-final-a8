from abc import ABC, abstractmethod 

class Ingredient(ABC):
    """
    Clase abstracta que define que propiedades van a tener los ingredientes

    Atributos
    ---------
        name: 
        quantity: 
        calories_per_100g:
        type:
        allergens: 

    Métodos
    ---------
        total_calories: devuelve el número de calorías según la cantidad
        is_allergen: devuelve True si el alimento contiene el alérgeno indicado
        str -> Muestra la información detalla del alimento
    """

    def __init__(self, name: str, quantity: float, calories_per_100g: float, type: str, allergens: list[str]):
        self.__name = name
        self.quantity = quantity
        self.calories_per_100g = calories_per_100g
        self.type = type
        self.allergens = allergens

    @property
    def name(self):
        return self.__name
    
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Cantidad ha de ser mayor a 1 gramo")
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
        return f"Información alimento: Ingredient[name='{self.name}', \
                quantity={self.quantity}, calories_per_100g={self.calories_per_100g}, \
                allergens={self.allergens}]"





    


