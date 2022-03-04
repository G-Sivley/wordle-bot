import unittest
import unittest.mock
import sys
import os
sys.path.insert(
    0, 
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../app'))
)
from word_handler import WordHandler
from letter import Letter


class TestWordHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wh = WordHandler()

    def test_is_correct_object(self):
        self.assertIsInstance(self.wh, WordHandler)

    def test_get_guess_str(self):
        with unittest.mock.patch("builtins.input", return_value="abide"):
            self.assertEqual(self.wh.get_guess_str(), "abide")
            
    def test_get_colors(self):
        with unittest.mock.patch("builtins.input", return_value="yrrgr"):
            self.assertEqual(self.wh.get_colors(), "yrrgr")
    
    def test_make_word(self):
        self.wh.guess_str = "abide"
        self.wh.colors = "rrgyr"
        self.wh.make_word()

        self.assertEqual(self.wh.word[1].character, "b")
        self.assertEqual(self.wh.word[3].color, "y")
        
