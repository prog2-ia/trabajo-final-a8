"""
Código para comprobar el funcionamiento de las clases "Ingredientes"
"""
from ingredients import AnimalIngredient 
from ingredients import MineralIngredient 
from ingredients import PlantIngredient


def main():

    # Crear ingredientes
    pollo = AnimalIngredient(
        "Pollo",
        200,
        239,
        [],
        "Pollo"
    )

    sal = MineralIngredient(
        "Sal",
        5,
        0,
        [],
        "Sal"
    )

    tomate = PlantIngredient(
        "Tomate",
        150,
        18,
        [],
        False
    )

    # Mostrar información
    print(pollo)
    print(sal)
    print(tomate)

    # Calcular calorías
    print("\nCalorías totales:")
    print(f"{pollo.name}: {pollo.total_calories()} kcal")
    print(f"{tomate.name}: {tomate.total_calories()} kcal")

    # Comprobar alérgenos
    print("\nComprobación de alérgenos:")
    print(f"¿Tomate contiene gluten? {tomate.is_allergen('gluten')}")
    print(f"¿Pollo contiene gluten? {pollo.is_allergen('gluten')}")

    # Método específico de AnimalIngredient
    print("\n¿Es carne?")
    print(f"{pollo.name}: {pollo.is_meat()}")


if __name__ == "__main__":
    main()