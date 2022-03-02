import unittest
from app.word import Word
from app.letter import Letter


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
