from .ingredient import Ingredient

class PlantIngredient(Ingredient):
    """
    Clase que representa un ingrediente de origen vegetal.

    Hereda de la clase Ingredient y añade información específica
    sobre si el ingrediente es una fruta o no.

    Attributes
    ----------
    __is_fruit : bool
        Indica si el ingrediente es una fruta (True) o no (False)
        
    """

    def __init__(self, name: str, quantity: float, calories_per_100g: float, allergens: list[str], is_fruit: bool) -> None:
        super().__init__(name, quantity, calories_per_100g, "PLANTA", allergens)
        self.is_fruit = is_fruit

    @property
    def is_fruit(self) -> bool:
        return self.__is_fruit
    
    @is_fruit.setter
    def is_fruit(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError("Indica si es fruta usando True o False")
        else:
            self.__is_fruit = value
