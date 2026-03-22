import pickle

def save_to_file(obj, filename):
    with open(filename, "wb") as f:
        pickle.dump(obj, f)

def load_from_file(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)
