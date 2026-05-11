"""
Código para ingredientes de origen mineral.

Define la clase MineralIngredient que extiende Ingredient con
información específica sobre el tipo de mineral del ingrediente.
"""


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
    def __init__(self, name: str, quantity: float, calories_per_100g: float, allergens: list[str], mineral_type: str) -> None:
        super().__init__(name, quantity, calories_per_100g, "MINERAL", allergens)
        self.mineral_type = mineral_type

    @property
    def mineral_type(self) -> str:
        """
        Obtiene el tipo de mineral del ingrediente.

        Returns:
            str: Tipo de mineral
        """
        return self.__mineral_type
    
    @mineral_type.setter
    def mineral_type(self, value: str) -> None:
        """
        Asigna el tipo de mineral del ingrediente.

        Args:
            value (str): Tipo de mineral

        Raises:
            ValueError: Si el valor no es una cadena de texto
        """
        # validar que el valor sea de tipo string
        if not isinstance(value, str):
            raise ValueError("Introduce el tipo de tipo usando letras")
        else:
            self.__mineral_type = value
