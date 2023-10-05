from src.models.ingredient import Ingredient, Restriction # noqa: F401, E261, E501

# Req 1
def test_ingredient():
    bacon1, bacon2 = Ingredient("bacon"), Ingredient("bacon")
    frango = Ingredient("frango")
    
    assert hash(bacon1) == hash(bacon2) and bacon1 == bacon2
    
    assert hash(bacon1) != hash(frango)
    
    assert bacon1 == bacon2
    assert bacon1 == bacon1
    
    assert bacon1 != frango
    
    assert repr(bacon1) == "Ingredient('bacon')"
    
    assert bacon1.name == "bacon"
    
    expected_bacon_restrictions = {Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED}
    assert bacon1.restrictions == expected_bacon_restrictions

def test_correct_implementation():
    try:
        test_ingredient()
        assert True
    except AssertionError:
        assert False
