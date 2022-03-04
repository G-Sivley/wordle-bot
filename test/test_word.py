import unittest
import sys
import os
sys.path.insert(
    0, 
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../app'))
)
from word import Word
from letter import Letter


class TestWord(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.word = Word("abide", ["r", "y", "g", "g", "r"])

    def test_init(self):
        self.assertEqual(self.word.word, "abide")
        self.assertEqual(self.word.list_of_word_states,
                         ["r", "y", "g", "g", "r"])

    def test_create_letters(self):
        letters_list = self.word.create_letters()
        self.assertIsInstance(letters_list[0], Letter)
        self.assertEqual(letters_list[2].character, "i")
        self.assertEqual(letters_list[1].index, 1)
