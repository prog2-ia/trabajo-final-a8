from abc import ABC, abstractmethod 

class Ingredient(ABC):
    """
    Clase abstracta que define que propiedades van a tener los ingredientes

    Atributos
    ---------

    id -> Número de identificación del alimento
    origen -> Origen del alimento
    fecha_caducidad -> Fecha de caducidad que tiene el alimento
    macro_nutrientes -> Lista de marconutrientes que aporta el alimento
    alergenos -> Lista de los alérgenos del alimento

    Funciones
    ---------
    str -> Muestra la información detalla del alimento

    """
    def __init__(self, id: int, origen: str, fecha_caducidad: str, macro_nutrientes: list, alergenos: list):
        self.__id = id
        self.__origen = origen
        self.__fecha_caducidad = fecha_caducidad
        self.__macro_nutrientes = macro_nutrientes
        self.__alergenos = alergenos

    @property
    def id(self):
        return self.__id
        
    @property
    def origen(self):
        return self.__origen
        
    @property
    def fecha_caducidad(self):
        return self.__fecha_caducidad

    @property
    def marco_nutrientes(self):
        return self.__macro_nutrientes
    
    @marco_nutrientes.setter
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
        return f"Información de ingrediente: id={self.id}, origen={self.origen},
                 fecha_caducidad={self.fecha_caducidad}, Macro-Nutrientes={self.macro_nutrientes}, 
                 Alérgenos={self.alergenos}"



    


