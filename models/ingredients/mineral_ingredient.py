from .ingredient import Ingredient

class MineralIngredient(Ingredient):
    """
    Clase que representa un ingrediente de origen mineral.

    Hereda de la clase Ingredient y añade información específica
    sobre el tipo de mineral del que procede el ingrediente
    (por ejemplo: sal, agua, etc.).

    Attributes
    ----------
    __mineral_type : str
        Tipo de mineral al que pertenece el ingrediente
        
    """
    def __init__(self, name, quantity, calories_per_100g, allergens, mineral_type: str):
        super().__init__(name, quantity, calories_per_100g, "MINERAL", allergens)
        self.mineral_type = mineral_type

    @property
    def mineral_type(self):
        return self.__mineral_type
    
    @mineral_type.setter
    def mineral_type(self, value):
        if not isinstance(value, str):
            raise ValueError("Introduce el tipo de tipo usando letras")
        else:
            self.__mineral_type = value
