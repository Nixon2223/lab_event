import unittest
from src.customer import Customer
from src.event import Event

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.event = Event("The Fringe", 55)
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
    
    def test_buy_ticket(self):
        self.assertEqual(45, self.customer.wallet)
        self.asserEqual(55, self.event.revenue)
        self.assertEqual(1, len(self.event.customer_list))
