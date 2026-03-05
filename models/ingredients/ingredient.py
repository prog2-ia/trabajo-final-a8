from abc import ABC, abstractmethod 

class Ingredient(ABC):
    """
    Clase abstracta que define que propiedades van a tener los ingredientes

    Atributos
    ---------

    id -> Número de identificación del alimento
    origen -> "ANIMAL", "VEGETAL" o "MINERAL"
    fecha_caducidad -> Fecha de caducidad ("dd/mm/yyy")
    macro_nutrientes -> Diccionario de marconutrientes que aporta el alimento
    Alergenos -> Lista de los alérgenos del alimento

    Funciones
    ---------
    str -> Muestra la información detalla del alimento

    """




    


