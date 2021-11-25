import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Bob", 100, "Drake")

    def test_get_wallet(self):
        self.assertEqual(100, self.customer.wallet)
    
    def test_decrease_wallet(self):
        self.customer.decrease_wallet(10)
        self.assertEqual(90, self.customer.wallet)
    
    def test_can_afford__True(self):
        self.assertEqual(True, self.customer.can_afford(55))
    
    def test_can_afford__False(self):
        self.assertEqual(False, self.customer.can_afford(200))
