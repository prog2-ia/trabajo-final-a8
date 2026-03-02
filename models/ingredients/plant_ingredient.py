from ingredient import Ingredient

class PlanIngredient(Ingredient):
    """
    Clase que define los alimentos de tipo planta
    """

    def __init__(self, id: int, origen: str, fecha_caducidad: str, contenido_fibra: float):
        super().__init__(id, origen, fecha_caducidad)
        self.origen = "VEGETAL"
        self.contenido_fibra = contenido_fibra

    @property

    


    def __str__(self):
        return f"Ingrediente animal: etc"
