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
    def __init__(self, id: int, origen: str, fecha_caducidad: str):
        self.__id = id
        self.__origen = origen
        self.__fecha_caducidad = fecha_caducidad

    @property
    def id(self):
        return self.__id
        
    @property
    def origen(self):
        return self.__origen
    
    @origen.setter
    def origen(self, value):
        if value not in ("ANIMAL", "VEGETAL", "MINERAL"):
            raise ValueError("Origen disponibles: 'ANIMAL', 'VEGETAL', 'MINERAL'")
        else:
            self.__origen = value

    @property
    def fecha_caducidad(self):
        return self.__fecha_caducidad
    
    @fecha_caducidad.setter
    def fecha_caducidad(self, fecha):
        if not isinstance(fecha, str):
            raise ValueError("Escriba la fecha con el siguiente formato: 'dd del mm del yyyy'")
        else:
            self.__fecha_caducidad = fecha

    def __str__(self):
        return f"Información de ingrediente: id={self.id}, origen={self.origen},
                 fecha_caducidad={self.fecha_caducidad}, Macro-Nutrientes={self.macro_nutrientes}, 
                 Alérgenos={self.alergenos}"



    


