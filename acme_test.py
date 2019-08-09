import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product("Test Product")
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """ Test default product price being 20."""
        prod = Product("Test Product")
        self.assertEqual(prod.weight, 20)

    def test_stealability_explode(self):
        """Test functionality of stealability and explode methods"""
        prod = Product("steal")
        prod.weight = 0.1
        self.assertEqual(prod.stealability(), "Very Stealable!")
        self.assertEqual(prod.explode(), "...fizzle")


class AcmeReportTests(unittest.TestCase):
    """ Testing for report module"""

    def test_default_num_products(self):
        """Test default length of product list"""
        list_of_products = generate_products()
        self.assertEqual(len(list_of_products), 30)

    def test_legal_names(self):
        """Test product name generation functionality"""
        names = [ADJECTIVES, NOUNS]
        list_of_products = generate_products()
        self.assertIn(list_of_products, names)


if __name__ == "__main__":
    unittest.main()
