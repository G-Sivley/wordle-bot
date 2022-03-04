import unittest
import sys
import os
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))
from letter import Letter


class Test_Letter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.letter = Letter("a", "g", 4)

    def test_init(self):
        self.assertEqual(self.letter.character, "a")
