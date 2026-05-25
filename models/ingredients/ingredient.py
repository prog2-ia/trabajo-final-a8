"""
Código para definir la estructura base de ingredientes.

Define la clase abstracta Ingredient que establece las propiedades
y comportamientos comunes a todos los tipos de ingredientes.
"""


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
        self.name = name
        self.quantity = quantity
        self.calories_per_100g = calories_per_100g
        self.type = type
        self.allergens = allergens

    @property
    def name(self) -> str:
        """
        Obtiene el nombre del ingrediente.
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Asigna el nombre del ingrediente.

        Args:
            value (str): Nombre del ingrediente

        Raises:
            ValueError: Si el nombre no es un string o contiene solo números
        """
        # validar que el atributo value es string
        if not isinstance(value, str):
            raise ValueError("El nombre debe ser un string")

        # validar que, aunque value sea un string, no se componga solo por dígitos
        if value.isdigit():
            raise ValueError("El nombre del ingrediente no puede contener solo números")

        self._name = value

    @property
    def quantity(self) -> float:
        """
        Obtiene la cantidad en gramos.
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value: float) -> None:
        """
        Asigna la cantidad en gramos.

        Args:
            value (float): Cantidad en gramos

        Raises:
            InvalidUnitError: Si la cantidad es menor o igual a 0
        """
        if value <= 0:
            raise InvalidUnitError("Cantidad ha de ser mayor a 0 gramos")
        else:
            self.__quantity = value

    @property
    def calories_per_100g(self) -> float:
        """
        Obtiene las calorías por cada 100 gramos.
        """
        return self.__calories_per_100g

    @calories_per_100g.setter
    def calories_per_100g(self, value: float) -> None:
        """
        Asigna las calorías por cada 100 gramos.

        Args:
            value (float): Calorías por 100g

        Raises:
            InvalidUnitError: Si el valor es negativo
        """
        if value < 0:
            raise InvalidUnitError("EL número de calorías ha de ser mayor que 0")
        else:
            self.__calories_per_100g = value

    @property
    def type(self) -> str:
        """
        Obtiene el tipo de ingrediente (animal, planta o mineral)
        """
        return self.__type

    @type.setter
    def type(self, value: str) -> None:
        """
        Asigna el tipo de ingrediente.

        Args:
            value (str): Tipo de ingrediente

        Raises:
            ValueError: Si el tipo no es válido
        """
        if value not in ("ANIMAL", "PLANTA", "MINERAL"):
            raise ValueError("Tipo de alimento no disponible")
        else:
            self.__type = value

    @property
    def allergens(self) -> list[str]:
        """
        Obtiene la lista de alérgenos.
        """
        return self.__allergens

    @allergens.setter
    def allergens(self, value: list[str]) -> None:
        """
        Asigna la lista de alérgenos.

        Args:
            value (list[str]): Lista de alérgenos

        Raises:
            ValueError: Si no es una lista o contiene elementos no string
        """
        # validar que sea una lista
        if not isinstance(value, list):
            raise ValueError("Hay que pasar los alérgenos empleando una lista")

        # validar que cada alérgeno sea un string
        for allergen in value:
            if not isinstance(allergen, str):
                raise ValueError("No introduzca números porfavor")
        else:
            self.__allergens = value

    def total_calories(self) -> float:
        """
        Calcula el total de calorías según la cantidad.

        Formula: (calorías_por_100g * cantidad) / 100

        Returns:
            float: Total de calorías del ingrediente
        """
        return (self.calories_per_100g * self.quantity) /100
    
    def is_allergen(self, allergen: str) -> bool:
        """
        Verifica si el ingrediente contiene un alérgeno específico.

        Args:
            allergen (str): Alérgeno a buscar

        Returns:
            bool: True si contiene el alérgeno, False en caso contrario

        Raises:
            ValueError: Si el parámetro no es una cadena de texto
        """
        if not isinstance(allergen, str):
            raise ValueError("Introduzca el alérgeno con letras porfavor")
        else:
            return allergen in self.allergens

    def __eq__(self, other: object) -> bool:
        """
        Compara dos ingredientes por nombre y tipo.
        """
        if not isinstance(other, Ingredient):
            return False

        return (
                self.name == other.name and
                self.type == other.type
        )

    def __str__(self) -> str:
        return f"Información alimento:\n -> Ingredient[name='{self.name}',\n-> quantity={self.quantity} \n-> calories_per_100g={self.calories_per_100g} \n-> allergens={self.allergens}]"

    def __repr__(self) -> str:
        return f"Ingredient(name={self.name}, type={self.type})"
