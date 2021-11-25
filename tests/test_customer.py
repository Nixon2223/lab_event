import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Bob", 100, "Drake")

    def test_get_wallet(self):
        self.assertEqual(100, self.customer.wallet)