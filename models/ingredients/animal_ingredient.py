from ingredient import Ingredient

class AnimalIngredient(Ingredient):
    def __init__(self, id: int, origen: str, fecha_caducidad: str, proteinas: float):
        super().__init__(id, origen, fecha_caducidad)
        self.__proteinas = proteinas

    @property
    def proteinas(self):
        return self.__proteinas
    
    def __str__(self):
        pass

