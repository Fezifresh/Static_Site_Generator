import unittest

from htmlnode import HTMLNode, LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        test_node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(test_node.to_html(), '<p>This is a paragraph of text.</p>')

    def test_to_html_2(self):
        test_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(test_node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_2(self):
        test_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(test_node.to_html(), '<a href="https://www.google.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()