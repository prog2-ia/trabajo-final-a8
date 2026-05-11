from pathlib import Path
import pickle


# carpeta donde se almacenan los pickle
PICKLE_DIR = Path("data/pickles")

# si no existe la carpeta, crearla
PICKLE_DIR.mkdir(parents=True, exist_ok=True)


def save_to_file(obj: object, filename: str) -> None:
    """
    Guarda objetos usando pickle.
    """

    file_path = PICKLE_DIR / filename
    with open(file_path, "wb") as f:
        pickle.dump(obj, f)


def load_from_file(filename: str) -> object:
    """
    Carga objetos desde un archivo pickle.
    """

    file_path = PICKLE_DIR / filename
    try:
        with open(file_path, "rb") as f:
            return pickle.load(f)

    except FileNotFoundError:
        raise FileNotFoundError(
            f"No existe el archivo '{filename}'"
        )