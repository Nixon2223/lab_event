import unittest
from src.performer import Performer

class TestPerformer(unittest.TestCase):

    def setUp(self):
        self.performer = Performer("Drake")
    
    def test_get_performer_name(self):
        self.assertAlmostEqual("Drake", self.performer.name)
    
