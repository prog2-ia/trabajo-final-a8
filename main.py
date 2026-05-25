"""
Código principal e interactivo para comprobar el funcionamiento de las
clases sobre ingredientes, platos y menús semanales.
"""

from models.dishes import Dish, MeatDish, MixedDish, VeganDish
from models.ingredients import Ingredient, AnimalIngredient, MineralIngredient, PlantIngredient
from models.weekly_menu import WeeklyMenu
from models.recipe_book import RecipeBook

from UI import exec


def initialize_sample_data() -> tuple[list[Ingredient], list[Dish]]:
    """
    Crea tres ingredientes y tres platos ya predefinidos.

    Returns:
        tuple[list[Ingredient], list[Dish]]: Tupla con listas de ingredientes y platos predefinidos
    """
    ingredientes: list[Ingredient] = []
    platos: list[Dish] = []

    # ingredientes predefinidos
    pollo = AnimalIngredient("Pechuga de Pollo", 500.0, 165.0, [], "Pollo")
    tomate = PlantIngredient("Tomate", 300.0, 18.0, [], True)
    sal = MineralIngredient("Sal", 50.0, 0.0, [], "Cloruro de Sodio")
    arroz = PlantIngredient("Arroz", 200.02, 130.0, [], False)
    huevo = AnimalIngredient("Huevo", 200.0, 130.0, [], False)
    ingredientes = [pollo, tomate, sal, arroz, huevo]

    # platos predefinidos
    plato1 = MeatDish("Pollo a la Plancha", [], 1)
    plato1.add_ingredient(pollo)

    plato2 = VeganDish("Ensalada", [], 1)
    plato2.add_ingredient(tomate)
    plato2.add_ingredient(sal)

    plato3 = MixedDish("Arroz con pollo", [], 1)
    plato3.add_ingredient(arroz)
    plato3.add_ingredient(pollo)
    plato3.add_ingredient(sal)

    platos = [plato1, plato2, plato3]

    return ingredientes, platos


def main() -> None:
    ingredientes, platos = initialize_sample_data()  # cargar datos predefinidos
    recetario = RecipeBook("Mi recetario")
    menu_semanal: WeeklyMenu | None = None
    exec(ingredientes, platos, recetario)

if __name__ == "__main__":
    main()
