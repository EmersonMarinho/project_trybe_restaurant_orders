import pytest
from src.models.dish import Dish, Ingredient  # noqa: F401, E261, E501


# Req 2
def test_dish():
    dish1 = Dish('Tomato', 2.5)
    dish2 = Dish('Garlic', 1.5)

    assert dish1.name == 'Tomato'

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish('Skito', '3156874')

    error_message = "Dish price must be greater then zero."
    with pytest.raises(ValueError, match=error_message):
        Dish('Jesus', -60)

    assert repr(dish1) == "Dish('Tomato', R$2.50)"
    assert dish1 == dish1
    assert dish1 != dish2

    assert hash(dish1) == hash(repr(dish1))
    assert hash(dish1) != hash(repr(dish2))

    dish1.add_ingredient_dependency(Ingredient('Salt'), 100)
    assert dish1.recipe == {Ingredient('Salt'): 100}
    assert dish1.get_ingredients() == set(dish1.recipe.keys())
    assert dish1.get_restrictions() == set()
