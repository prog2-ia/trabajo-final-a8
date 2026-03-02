from ingredient import Ingredient

class MineralIngredient(Ingredient):
    def __init__(self, id: int, origen: str, fecha_caducidad: str, minerales: list):
        super().__init__(id, origen, fecha_caducidad, minerales)
        self.__minerales = minerales