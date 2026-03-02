from ingredient import Ingredient

class MineralIngredient(Ingredient):
    """
    Clase que define los ingredientes de origen Mineral
    """
    def __init__(self, id: int, origen: str, fecha_caducidad: str, minerales: list):
        super().__init__(id, origen, fecha_caducidad, minerales)
        self.origen = "MINERAL"
        self.__minerales = minerales