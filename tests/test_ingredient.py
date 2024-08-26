from praktikum.ingredient import Ingredient
from test_data import TestData

class TestIngredient:

    def test_get_price(self):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, TestData.INGREDIENT_NAME, TestData.INGREDIENT_PRICE )

        assert ingredient.get_price() == TestData.INGREDIENT_PRICE

    def test_get_name(self):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, TestData.INGREDIENT_NAME, TestData.INGREDIENT_PRICE)

        assert ingredient.get_name() == TestData.INGREDIENT_NAME

    def test_get_type(self):
        ingredient = Ingredient(TestData.INGREDIENT_TYPE, TestData.INGREDIENT_NAME, TestData.INGREDIENT_PRICE)

        assert ingredient.get_type() == TestData.INGREDIENT_TYPE