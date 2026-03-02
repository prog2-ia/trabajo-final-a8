from ingredient import Ingredient

class AnimalIngredient(Ingredient):
    """
    Clase que define la información de alimentos de origen animal
    """
    def __init__(self, id: int, origen: str, fecha_caducidad: str, crianza: str, macro_nutrientes: list, alergenos: list):
        super().__init__(id, origen, fecha_caducidad)
        self.origen = "ANIMAL"
        self.crianza = crianza
        self.macro_nutrientes = macro_nutrientes
        self.alergenos = alergenos

    @property
    def crianza(self):
        return self.__crianza
    
    @crianza.setter
    def crianza(self, metodo):
        if metodo not in ("ECOLÓGICO", "INTENSIVO"):
            raise ValueError("Métodos disponibles: 'ECOLÓGICO', 'INTENSIVO")
        else:
            self.__crianza = metodo

    @property
    def macro_nutrientes(self):
        return self.__macro_nutrientes
    
    @macro_nutrientes.setter
    def macro_nutrientes(self, nutrientes: list):
        if not nutrientes.strip():
            raise ValueError("La lista de nutrientes no puede estar vacía")
        else:
            self.macro_nutrientes.append(nutrientes)

    @property
    def alergenos(self):
        return self.__alergenos
    
    @alergenos.setter
    def alergenos(self, lista_alergenos: list):
        if not lista_alergenos.strip():
            raise ValueError("La lista de alérgenos no puede estar vacía")
        else:
            self.__alergenos.append(lista_alergenos)

    def __str__(self):
        return super().__str__()
            
