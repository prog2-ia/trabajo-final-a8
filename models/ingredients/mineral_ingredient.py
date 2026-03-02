from ingredient import Ingredient

class MineralIngredient(Ingredient):
    """
    Clase que define los ingredientes de origen Mineral
    """
    def __init__(self, id: int, origen: str, fecha_caducidad: str, minerales: list):
        super().__init__(id, origen, fecha_caducidad, minerales)
        self.origen = "MINERAL"
        self.__minerales = minerales

    @property
    def minerales(self):
        return self.__minerales
    
    @minerales.setter
    def minerales(self, lista_minerales: list):
        if not lista_minerales.strip():
            raise ValueError("Error")
        else:
            self.__minerales += lista_minerales