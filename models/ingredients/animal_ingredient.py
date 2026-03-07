from ingredient import Ingredient

class AnimalIngredient(Ingredient):
    """
    Clase que define la información de alimentos de origen animal
    """
    def __init__(self, name, quantity, calories_per_100g, type, allergens, animal_source: str):
        super().__init__(name, quantity, calories_per_100g, type, allergens)
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

    def is_meat(self, type):
        if type == "meat":
            return True            

    def __str__(self):
        super().__str__()