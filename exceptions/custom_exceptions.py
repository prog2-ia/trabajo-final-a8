"""
Código de excepciones personalizadas.
"""


class InvalidUnitError(Exception):
    """
    Se lanza cuando una unidad numérica es inválida.
    """
    pass


class IncompatibleIngredientError(Exception):
    """
    Se lanza cuando un ingrediente no es compatible
    con el tipo de plato.
    """
    pass


class InvalidServingError(Exception):
    """
    Se lanza cuando el número de raciones es inválido.
    """
    pass
