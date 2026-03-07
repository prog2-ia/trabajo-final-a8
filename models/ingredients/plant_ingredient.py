from .ingredient import Ingredient

class PlantIngredient(Ingredient):
    """
    Clase que define los alimentos de tipo planta
    """

    def __init__(self, name, quantity, calories_per_100g, allergens, is_fruit: bool):
        super().__init__(name, quantity, calories_per_100g, "PLANTA", allergens)
        self.is_fruit = is_fruit

    @property
    def is_fruit(self):
        return self.__is_fruit
    
    @is_fruit.setter
    def is_fruit(self, value):
        if not isinstance(value, bool):
            raise ValueError("Indica si es fruta usando True o False")
        else:
            self.__is_fruit = value
