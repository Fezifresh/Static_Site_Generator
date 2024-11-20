import unittest

from markdown_to_blocks import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_eq(self):
        text = "### Heading 3"
        self.assertEqual(block_to_block_type(text), BlockType.HEADING)

    def test_eq_2(self):
        text = "```\nTHIS IS CODE\n```"
        self.assertEqual(block_to_block_type(text), BlockType.CODE)
        
    def test_eq_3(self):
        text = "> I am become death\n> or whatever"
        self.assertEqual(block_to_block_type(text), BlockType.QUOTE)

    def test_eq_4(self):
        text = "- butter\n- eggs\n- flour"
        self.assertEqual(block_to_block_type(text), BlockType.UNORDERED)

    def test_eq_5(self):
        text = "1. FC Bayern\n2. Hajduk Split\n3. HSV"
        self.assertEqual(block_to_block_type(text), BlockType.ORDERED)

    def test_eq_6(self):
        text = "2. - ### Heading 3´´´"
        self.assertEqual(block_to_block_type(text), BlockType.TEXT)

    def test_eq_7(self):
        text = "This is just regular text"
        self.assertEqual(block_to_block_type(text), BlockType.TEXT)

if __name__ == "__main__":
    unittest.main()