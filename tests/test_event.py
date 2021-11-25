import unittest
from src.customer import Customer
from src.performer import Performer
from src.event import Event

class TestEvent(unittest.TestCase):

    def setUp(self):
        self.event = Event("The Fringe", 55)

    def test_get_ticket_price(self):
        self.assertEqual(55, self.event.ticket_price)

