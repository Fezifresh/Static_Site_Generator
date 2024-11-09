import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("I am a test file", TextType.ITALIC)
        node2 = TextNode("I am a test file", TextType.ITALIC, None)
        self.assertEqual(node, node2)

    def test_eq_3(self):
        node = TextNode("I am a test file", TextType.LINK, "www.google.com")
        node2 = TextNode("I am a test file", TextType.LINK, "www.google.com")
        self.assertEqual(node, node2)
        
    def test_not_eq(self):
        node = TextNode("I am a test file", TextType.LINK, "www.google.com")
        node2 = TextNode("I am a test file", TextType.IMAGE, "www.google.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_2(self):
        node = TextNode("I am also a test file", TextType.NORMAL, "www.google.com")
        node2 = TextNode("I am a test file", TextType.NORMAL, "www.google.com")
        self.assertNotEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("I am a test file", TextType.CODE, "None")
        node2 = TextNode("I am a test file", TextType.CODE,)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()