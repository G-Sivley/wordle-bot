import unittest
import pathlib as pl
import sys
sys.path.append("../")
from app.data_manipulator import DataManipulator


class TestDataManipulator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dm = DataManipulator()

    def test_class_init(self):
        self.assertIsInstance(self.dm, DataManipulator)

    def test_write_remaining_possible_answers(self):
        path = pl.Path("word lists/remaining_possible_answers.txt")
        self.assertEquals((str(path), path.is_file()), (str(path), True))

    def test_is_letter_in_word(self):
        self.assertEqual(self.dm.is_letter_in_word("a", "abott"), True)
        self.assertEqual(self.dm.is_letter_in_word("a", "plane"), True)
        self.assertEqual(self.dm.is_letter_in_word("z", "coins"), False)
        self.assertEqual(self.dm.is_letter_in_word("A", "plane"), True)

    def test_remove_excluded_answers(self):
        self.assertEqual(self.dm.remove_words_from_list_with_letter([
            "alpha",
            "wow",
            "brittle",
        ], "a"), ["wow", "brittle"])
        self.assertEqual(self.dm.remove_words_from_list_with_letter([
            "alpha",
            "heart",
            "hobbs",
        ], "h"), [])

    def test_remove_lines_with_words_in_index(self):
        self.assertEqual(self.dm.remove_lines_with_words_in_index([
            "artsy",
            "augur",
            "birch",
            "conch",
            "comma",
            "crawl"
            ], "r", 1), ["augur", "birch", "conch", "comma"])

        self.assertEqual(self.dm.remove_lines_with_words_in_index([
            "could",
            "cough",
            "craze",
            "owner",
            "pause",
            "pique"
            ], "u", 2), ["craze", "owner", "pique"])

