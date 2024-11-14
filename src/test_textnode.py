import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode, HTMLNode

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
        node = TextNode("I am also a test file", TextType.TEXT, "www.google.com")
        node2 = TextNode("I am a test file", TextType.TEXT, "www.google.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_3(self):
        node = TextNode("I am a test file", TextType.CODE, "None")
        node2 = TextNode("I am a test file", TextType.CODE,)
        self.assertNotEqual(node, node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(text_node_to_html_node(node).to_html(), "<b>This is a text node</b>")

    def test_eq_2(self):
        node = TextNode("I am a test file", TextType.LINK, "www.google.com")
        self.assertEqual(text_node_to_html_node(node).to_html(), "<a href=\"www.google.com\">I am a test file</a>")

    def test_eq_3(self):
        node = TextNode("I am a test image", TextType.IMAGE, "www.my.image.com")
        self.assertEqual(text_node_to_html_node(node).to_html(), "<img src=\"www.my.image.com\" alt=\"I am a test image\"></img>")

if __name__ == "__main__":
    unittest.main()