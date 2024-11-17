import unittest

from markdown_to_blocks import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_eq(self):
        text = "### Heading 3"
        self.assertEqual(block_to_block_type(text), "Heading")

    def test_eq_2(self):
        text = "```THIS IS CODE```"
        self.assertEqual(block_to_block_type(text), "Code")
        
    def test_eq_3(self):
        text = ">I am become death\n>or whatever"
        self.assertEqual(block_to_block_type(text), "Quote")

    def test_eq_4(self):
        text = "- butter\n- eggs\n- flour"
        self.assertEqual(block_to_block_type(text), "Unordered List")

    def test_eq_5(self):
        text = "1. FC Bayern\n2. Hajduk Split\n3. HSV"
        self.assertEqual(block_to_block_type(text), "Ordered List")

    def test_eq_6(self):
        text = "2. - ### Heading 3´´´"
        self.assertEqual(block_to_block_type(text), "Normal Text")

if __name__ == "__main__":
    unittest.main()