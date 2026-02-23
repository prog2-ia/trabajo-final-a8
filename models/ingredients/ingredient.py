from abc import ABC, abstractmethod 

class Ingredient(ABC):
    """
    Clase abstracta que define que propiedades van a tener los ingredientes
    """

    def __init__(self, origen) -> None:
        self.__origen = origen

    @property
    def origen(self):
        return self.__origen
    


