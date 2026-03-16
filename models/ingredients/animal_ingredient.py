from .ingredient import Ingredient

class AnimalIngredient(Ingredient):
    """
    Clase que representa un ingrediente de origen animal.

    Hereda de la clase Ingredient y añade información específica
    sobre el animal del que procede el ingrediente.

    Attributes
    ----------
    __animal_source : str
        Animal del que procede el ingrediente (por ejemplo: cerdo, vaca, pollo)
        
    """
    def __init__(self, name, quantity, calories_per_100g, allergens, animal_source: str):
        super().__init__(name, quantity, calories_per_100g, "ANIMAL", allergens)
        self.animal_source = animal_source

    @property
    def animal_source(self):
        return self.__animal_source
    
    @animal_source.setter
    def animal_source(self, value):
        if not isinstance(value, str):
            raise ValueError("Introduzca el animal con letras porfavor")
        else:
            self.__animal_source = value

    def is_meat(self):
        if self.animal_source in ['Cerdo', 'Vaca', 'Pollo']:
            return True
        else:
            return False        

