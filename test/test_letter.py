import unittest
from app.letter import Letter


class Test_Letter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.letter = Letter("a", "g", 4)

    def test_init(self):
        self.assertEqual(self.letter.character, "a")
