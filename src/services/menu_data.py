import csv

from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        self._parse_csv(source_path)

    def _parse_csv(self, source_path: str):
        dish_cache = {}

        with open(source_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                dish_name, dish_price, ingredient_name, recipe_amount = row

                dish_price = float(dish_price)

                if dish_name not in dish_cache:
                    dish = Dish(dish_name, dish_price)
                    dish_cache[dish_name] = dish
                    self.dishes.add(dish)
                else:
                    dish = dish_cache[dish_name]

                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, int(recipe_amount))
