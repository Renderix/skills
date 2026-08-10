import unittest

from calculator import price_after_discount


class PriceAfterDiscountTests(unittest.TestCase):
    def test_applies_discount(self):
        self.assertEqual(80, price_after_discount(100, 20))

    def test_zero_discount_preserves_price(self):
        self.assertEqual(100, price_after_discount(100, 0))


if __name__ == "__main__":
    unittest.main()
