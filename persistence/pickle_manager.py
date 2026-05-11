"""
Código para serializar y deserializar objetos usando pickle.

Gestiona la persistencia de objetos en archivos, con soporte para
crear automáticamente el directorio de almacenamiento.
"""


from pathlib import Path
import pickle


# directorio donde se almacenan los pickle
PICKLE_DIR = Path("data/pickles")

# si no existe la carpeta, crearla
PICKLE_DIR.mkdir(parents=True, exist_ok=True)


def save_to_file(obj: object, filename: str) -> None:
    """
    Serializa y guarda un objeto en un archivo pickle.

    Args:
        obj (object): Objeto a serializar
        filename (str): Nombre del archivo donde guardar

    Returns:
        None
    """

    file_path = PICKLE_DIR / filename
    with open(file_path, "wb") as f:
        pickle.dump(obj, f)


def load_from_file(filename: str) -> object:
    """
    Carga y deserializa un objeto desde un archivo pickle.

    Args:
        filename (str): Nombre del archivo a cargar

    Returns:
        object: Objeto deserializado desde el archivo

    Raises:
        FileNotFoundError: Si el archivo no existe en el directorio pickle
    """

    file_path = PICKLE_DIR / filename
    try:
        with open(file_path, "rb") as f:
            return pickle.load(f)

    except FileNotFoundError:
        raise FileNotFoundError(
            f"No existe el archivo '{filename}'"
        )
