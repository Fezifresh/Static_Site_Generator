import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_eq(self):
        text = "      # This is a heading             \n\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        self.assertEqual(extract_title(text), "This is a heading")
    
    def test_eq_2(self):
        text = "# This is a heading"
        self.assertEqual(extract_title(text), "This is a heading")

    def test_eq_3(self):
        text = "## This is a heading"
        self.assertRaises(Exception)
           
    
if __name__ == "__main__":
    unittest.main()