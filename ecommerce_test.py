import unittest
from ecommerce import Order, Customer

class EcommerceTests(unittest.TestCase):
    
    def setUp(self):
        self.order = Order()
        self.customer = Customer()
        
    def place_order_test(self):