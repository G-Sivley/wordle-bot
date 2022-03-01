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
        self.assertEqual(self.dm.remove_excluded_answers([
            "alpha",
            "wow",
            "brittle",
        ], "a"), ["wow", "brittle"])
        self.assertEqual(self.dm.remove_excluded_answers([
            "alpha",
            "heart",
            "hobbs",
        ], "h"), [])