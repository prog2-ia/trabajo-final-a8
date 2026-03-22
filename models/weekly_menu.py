class WeeklyMenu:
    def __init__(self):
        self.menu = {}

    def add_day(self, day, dish):
        self.menu[day] = dish

    def total_calories(self):
        return sum(dish.total_calories() for dish in self.menu.values())

    def __add__(self, other):
        shopping_list = {}

        for menu in [self, other]:
            for dish in menu.menu.values():
                for ing in dish.ingredients:
                    if ing.name in shopping_list:
                        shopping_list[ing.name] += ing.quantity
                    else:
                        shopping_list[ing.name] = ing.quantity

        return shopping_list

    def __gt__(self, other):
        return self.total_calories() > other.total_calories()

    def __lt__(self, other):
        return self.total_calories() < other.total_calories()

    def __str__(self):
        return "\n".join([f"{day}: {dish.name}" for day, dish in self.menu.items()])
