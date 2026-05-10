from models.dishes.dish import Dish


class RecipeBook:
    def __init__(self, name: str) -> None:
        self.name = name
        self.dishes = []

    def add_dish(self, dish: Dish) -> None:
        if dish in self.dishes:
            raise ValueError("El plato ya existe")
        self.dishes.append(dish)

    def remove_dish(self, dish: Dish) -> None:
        self.dishes.remove(dish)

    def filter_by_type(self, dish_type: str) -> list[Dish]:
        return [d for d in self.dishes if d.dish_type == dish_type]

    def filter_by_allergen(self, allergen: str) -> list[Dish]:
        return [d for d in self.dishes if not d.contains_allergen(allergen)]

    def __len__(self):
        return len(self.dishes)

    def __str__(self):
        return "\n".join([dish.name for dish in self.dishes])
