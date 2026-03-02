from abc import ABC, abstractmethod 

class Dish(ABC):
    """
    Clase abstracta de la que heredan los tipos de platos
    """
    def __init__(self, macro_nutrientes: list, origen: float):
        