from models.dishes.dish import Dish


class WeeklyMenu:
    def __init__(self) -> None:
        self.menu = {}

    def add_day(self, day: str, dish: Dish) -> None:
        self.menu[day] = dish

    def total_calories(self) -> float:
        return sum(dish.total_calories() for dish in self.menu.values())

    def __add__(self, other: "WeeklyMenu") -> dict[str, float]:
        shopping_list = {}

        for menu in [self, other]:
            for dish in menu.menu.values():
                for ing in dish.ingredients:
                    if ing.name in shopping_list:
                        shopping_list[ing.name] += ing.quantity
                    else:
                        shopping_list[ing.name] = ing.quantity

        return shopping_list

    def __gt__(self, other: "WeeklyMenu") -> bool:
        return self.total_calories() > other.total_calories()

    def __lt__(self, other: "WeeklyMenu") -> bool:
        return self.total_calories() < other.total_calories()

    def __getitem__(self, day: str) -> Dish:
        return self.menu[day]

    def __str__(self) -> str:
        return "\n".join([f"{day}: {dish.name}" for day, dish in self.menu.items()])
