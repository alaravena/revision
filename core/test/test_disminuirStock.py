import unittest
from core.views import test_disminuir_stock

class TestDisminuirStock(unittest.TestCase):

    def test_disminuirStock(self):
        stock = 5
        self.assertNotEqual(test_disminuir_stock(stock), stock)


if __name__ ==  "__main__":
    unittest.main()