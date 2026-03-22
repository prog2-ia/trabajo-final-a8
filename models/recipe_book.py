class RecipeBook:
    def __init__(self, name):
        self.name = name
        self.dishes = []

    def add_dish(self, dish):
        if dish in self.dishes:
            raise ValueError("El plato ya existe")
        self.dishes.append(dish)

    def remove_dish(self, dish):
        self.dishes.remove(dish)

    def filter_by_type(self, dish_type):
        return [d for d in self.dishes if d.dish_type == dish_type]

    def filter_by_allergen(self, allergen):
        return [d for d in self.dishes if not d.contains_allergen(allergen)]

    def __str__(self):
        return "\n".join([dish.name for dish in self.dishes])
