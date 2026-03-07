"""
Código para comprobar el funcionamiento de las clases "Ingredientes"
"""
from .animal_ingredient import AnimalIngredient 
from .mineral_ingredient import MineralIngredient 
from .plant_ingredient import PlantIngredient


pollo = AnimalIngredient(
    "Pollo",
    200,
    239,
    "ANIMAL",
    ["protein"],
    "Pollo"
)

sal = MineralIngredient(
    "Sal",
    5,
    0,
    "MINERAL",
    [],
    "Sal"
)

tomate = PlantIngredient(
    "Tomate",
    150,
    18,
    "PLANTA",
    [],
    False
)

print(pollo.total_calories())
print(tomate.is_allergen("gluten"))
print(sal)