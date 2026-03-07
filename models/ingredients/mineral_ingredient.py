from ingredient import Ingredient

class MineralIngredient(Ingredient):
    """
    Clase que define los ingredientes de origen Mineral

    Atributos
    ---------
        -name: Nombre
        - quantity: ...
    """
    def __init__(self, name, quantity, calories_per_100g, type, allergens, mineral_type: str):
        super().__init__(name, quantity, calories_per_100g, type, allergens)
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


    def total_calories(self):
        super().total_calories()

    def is_allergen(self, value):
        super().is_allergen(value)

    def __str__(self):
        super().__str__()
