import unittest
from src.customer import Customer
from src.performer import Performer
from src.event import Event

class TestEvent(unittest.TestCase):

    def setUp(self):
        self.event = Event("The Fringe", 55)
        self.customer1 = Customer("Bob", 100, "Drake")
        self.customer2 = Customer("Paul", 60, "Mily Cyrus")
        self.performer1 = Performer("Drake")
        self.performer2 =  Performer("AC/DC")
        self.event.customer_list = [self.customer1, self.customer2]
        self.event.performer_list = [self.performer1, self.performer2]

    def test_get_ticket_price(self):
        self.assertEqual(55, self.event.ticket_price)

    def test_increase_revenue(self):
        self.event.increase_revenue()
        self.assertEqual(55, self.event.revenue)

