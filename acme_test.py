#!/usr/bin/env python

import unittest
from acme import Product, BoxingGlove


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    def test_default_profuct_weight(self):
        '''tests if weight is default 20'''
        prod = Product('Test Product')
        self.assertionEqual(prod.price, 20)
    def test_case_1(self):
        '''sees if this product does correctly'''
        prod = Product(name ='TestProduct', price = 30, weight = 10, flammability = 2)
        self.assertEqual(prod.stealability(), 'Very stealable!')
        self.assertEqual(prod.explode(), '...boom!')

class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        '''making sure the list defaults to 30'''
        count = generate_products(Product)
        self.assertEqual(prod_name_list, 30)
    def test_legal_names(self):
        '''seeing if the names are all in proper form'''
        self.assertIn(prod.name[0][0],list1)
        self.assertIn(prod.name[0][1],list2)
        
if __name__ == '__main__':
    unittest.main()
