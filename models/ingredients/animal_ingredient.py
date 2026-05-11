"""
Código para ingredientes de origen animal.

Define la clase AnimalIngredient que extiende Ingredient con
información específica sobre el animal de procedencia del ingrediente.
"""


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
    def __init__(self, name: str, quantity: float, calories_per_100g: float, allergens: list[str], animal_source: str) -> None:
        super().__init__(name, quantity, calories_per_100g, "ANIMAL", allergens)
        self.animal_source = animal_source

    @property
    def animal_source(self) -> str:
        """
        Obtiene el tipo de animal del ingrediente.

        Returns:
            str: Animal de procedencia
        """
        return self.__animal_source
    
    @animal_source.setter
    def animal_source(self, value: str) -> None:
        """
        Asigna el tipo de animal del ingrediente.

        Args:
            value (str): Tipo de animal

        Raises:
            ValueError: Si el valor no es una cadena de texto
        """
        # validar que el valor sea de tipo str
        if not isinstance(value, str):
            raise ValueError("Introduzca el animal con letras porfavor")
        else:
            self.__animal_source = value

    def is_meat(self) -> bool:
        """
        Verifica si el ingrediente es carne (cerdo, vaca o pollo).

        Returns:
            bool: True si es carne, False si es otro producto animal
        """
        # Verificar si el animal es una fuente de carne común
        if self.animal_source in ['Cerdo', 'Vaca', 'Pollo']:
            return True
        else:
            return False        

