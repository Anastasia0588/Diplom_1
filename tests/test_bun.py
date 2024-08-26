from praktikum.bun import Bun
from test_data import TestData


class TestBun:

    def test_get_name(self):
        bun = Bun(TestData.BUN_NAME, TestData.BUN_PRICE)

        assert bun.get_name() == TestData.BUN_NAME

    def test_get_price(self):
        bun = Bun(TestData.BUN_NAME, TestData.BUN_PRICE)

        assert bun.get_price() == TestData.BUN_PRICE

