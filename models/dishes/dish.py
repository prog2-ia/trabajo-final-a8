"""
Código para la clase base abstracta de platos.

Define la estructura común que deben tener todos los tipos de platos
del sistema (carne, vegano, mixto) incluyendo gestión de ingredientes,
calorías y validaciones.
"""


from abc import ABC, abstractmethod
from ..ingredients import Ingredient
from exceptions.custom_exceptions import InvalidServingError


class Dish(ABC):
    """
    Clase abstracta que representa un plato.

    Esta clase define la estructura común que tendrán todos los tipos de platos
    del sistema. No debe instanciarse directamente, sino que debe heredarse
    para crear tipos concretos de platos (por ejemplo, platos veganos o de carne).

    Attributes
    ----------
    _name : str
        Nombre del plato.
    __ingredients : list[Ingredient]
        Lista de ingredientes que componen el plato.
    __servings : int
        Número de raciones del plato.
    __dish_type : str
        Tipo de plato. Puede ser "CARNE", "VEGANO" o "MIXTO".
    """

    def __init__(self, name: str, ingredients: list[Ingredient], servings: int, dish_type: str) -> None:
        self._name = name
        self.ingredients = ingredients
        self.servings = servings
        self.dish_type = dish_type

    @property
    def name(self) -> str:
        """
        Obtiene el nombre del plato.
        """
        return self._name
    
    @property
    def ingredients(self) -> list[Ingredient]:
        """
        Obtiene la lista de ingredientes.
        """
        return self.__ingredients
    
    @ingredients.setter
    def ingredients(self, value: list[Ingredient]) -> None:
        """
        Asigna la lista de ingredientes.

        Args:
            value (list[Ingredient]): Lista de ingredientes

        Raises:
            ValueError: Si no es una lista o contiene elementos no Ingredient
        """
        # validar que sea una lista
        if not isinstance(value, list):
            raise ValueError("Incluye los ingredientes usando una lista")

        # Validar que cada elemento sea un Ingredient
        for ingredient in value:
            if not isinstance(ingredient, Ingredient):
                raise ValueError("Utiliza objetos ingrediente")
        else:
            self.__ingredients = value

    @property
    def servings(self) -> int:
        """
        Obtiene el número de raciones.
        """
        return self.__servings
    
    @servings.setter
    def servings(self, value: int) -> None:
        """
        Asigna el número de raciones.

        Args:
            value (int): Número de raciones

        Raises:
            InvalidServingError: Si el valor es menor o igual a 0
        """
        if value <= 0:
            raise InvalidServingError("El número de raciones ha de ser mayor que 0")
        else:
            self.__servings = value

    @property
    def dish_type(self) -> str:
        """Obtiene el tipo de plato."""
        return self.__dish_type
    
    @dish_type.setter
    def dish_type(self, value: str) -> None:
        """
        Asigna el tipo de plato.

        Args:
            value (str): Tipo de plato (CARNE, VEGANO o MIXTO)

        Raises:
            ValueError: Si el tipo no es válido
        """
        if value not in ("CARNE", "VEGANO", "MIXTO"):
            raise ValueError("Tipos de platos: 'CARNE', 'VEGANO', 'MIXTO'")
        else:
            self.__dish_type = value

    # Métodos

    def add_ingredient(self, ingredient: Ingredient) -> None:
        """
        Añade un ingrediente al plato si no existe duplicado.

        Args:
            ingredient (Ingredient): Ingrediente a añadir

        Raises:
            ValueError: Si el ingrediente no es válido o ya existe
        """
        if not isinstance(ingredient, Ingredient):
            raise ValueError("Usa objetos ingrediente")

        # verificar que no exista un ingrediente con el mismo nombre
        for i in self.ingredients:
            if i.name == ingredient.name:
                raise ValueError("El alimento ya existe en el plato")
        else:
            self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient: Ingredient) -> bool:
        """
        Elimina un ingrediente del plato.

        Args:
            ingredient (Ingredient): Ingrediente a eliminar

        Returns:
            bool: True si se eliminó correctamente, False si no existe

        Raises:
            ValueError: Si el parámetro no es un Ingredient válido
        """
        if not isinstance(ingredient, Ingredient):
            raise ValueError("Usa objetos ingrediente")

        # buscar y eliminar el ingrediente por nombre
        for i in self.ingredients:
            if i.name == ingredient.name:
                self.ingredients.remove(i)
                return True
        return False
        
    def total_calories(self) -> float:
        """
        Calcula el total de calorías del plato.

        Returns:
            float: Suma de calorías de todos los ingredientes
        """
        total = 0
        for ingredient in self.ingredients:
            total += ingredient.total_calories()
        return total

    def calories_per_ingredient(self) -> list[list]:
        """
        Obtiene las calorías de cada ingrediente del plato.

        Returns:
            list[list]: Lista con formato [[nombre, calorías], ...]
        """
        calories = []
        for ingredient in self.ingredients:
            calories.append([ingredient.name, ingredient.total_calories()])
        return calories

    def contains_allergen(self, allergen: str) -> bool:
        """
        Verifica si el plato contiene un alérgeno específico.

        Args:
            allergen (str): Alérgeno a buscar

        Returns:
            bool: True si el plato contiene el alérgeno, False en caso contrario

        Raises:
            ValueError: Si el alérgeno no es una cadena de texto
        """
        if not isinstance(allergen, str):
            raise ValueError("El alérgeno debe ser un string")

        # Verificar si algún ingrediente contiene el alérgeno
        for ingredient in self.ingredients:
            if ingredient.is_allergen(allergen):
                return True
        return False      
    
    def list_ingredients(self) -> list[str]:
        """
        Obtiene la lista de nombres de ingredientes.

        Returns:
            list[str]: Lista de nombres de ingredientes
        """
        return [ingredient.name for ingredient in self.ingredients]
    
    @abstractmethod
    def is_vegan(self) -> bool:
        """
        Verifica si el plato es vegano.
        Debe ser implementado en subclases según su tipo.

        Returns:
            bool: True si el plato es vegano, False en caso contrario
        """
        pass

    @abstractmethod
    def is_meat(self) -> bool:
        """
        Verifica si el plato contiene carne.
        Debe ser implementado en subclases según su tipo.

        Returns:
            bool: True si el plato contiene carne, False en caso contrario
        """
        pass

    def __eq__(self, other: object) -> bool:
        """
        Compara dos platos por nombre.
        """
        if not isinstance(other, Dish):
            return False
        return self.name == other.name

    def __str__(self) -> str:
        return (f"Información del plato: \n"
                f"Nombre='{self.name}'\n"
                f"Tipo='{self.dish_type}' \n"
                f"Ingredientes: {self.list_ingredients()} \n"
                f"Calorías totales={self.total_calories()}")

    def __repr__(self) -> str:
        return f"Dish({self.name}, {self.dish_type})"
