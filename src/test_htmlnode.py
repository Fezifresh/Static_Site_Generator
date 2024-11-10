import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        test_node = HTMLNode(None, None, None, {
    "href": "https://www.google.com", 
    "target": "_blank",
})
        self.assertEqual(test_node.props_to_html(),' href="https://www.google.com" target="_blank"')

    def test_props_2(self):
        test_node = HTMLNode("p", "test text here", None, {
    "href": "https://www.google.com", 
    "target": "_blank",
    "info": "nothing here",
})
        self.assertEqual(test_node.props_to_html(),' href="https://www.google.com" target="_blank" info="nothing here"')

    def test_props_3(self):
        test_node = HTMLNode("p", None, None, None)
        self.assertRaises(ValueError)


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


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        test_node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        self.assertEqual(test_node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')
    
    def test_to_html_2(self):
        test_node = ParentNode(
    "p",
    [
        ParentNode(
    "p",
    [
        LeafNode("b", "Nested Bold text"),
        LeafNode(None, "Nested Normal text"),
    ],
),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        self.assertEqual(test_node.to_html(), '<p><p><b>Nested Bold text</b>Nested Normal text</p>Normal text<i>italic text</i>Normal text</p>')

    def test_to_html_3(self):
        test_node = ParentNode(
    "p",
    [
        ParentNode(
    "p",
    [
        ParentNode(
    "p",
    [
        LeafNode(None, "Double Nested Normal text"),
    ],
),
        LeafNode(None, "Nested Normal text"),
    ],
),
        LeafNode(None, "Normal text"),
    ],
)
        self.assertEqual(test_node.to_html(), '<p><p><p>Double Nested Normal text</p>Nested Normal text</p>Normal text</p>')

    def test_to_html_4(self):
        test_node = ParentNode("p", None)
        self.assertRaises(ValueError)

    def test_to_html_5(self):
        test_node = ParentNode(
    "p",
    [
        LeafNode(None, "Normal text"),
        ParentNode(
    "p",
    [
        LeafNode("b", "Nested Bold text"),
        LeafNode(None, "Nested Normal text"),
    ],
),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
    ],
)
        self.assertEqual(test_node.to_html(), '<p>Normal text<p><b>Nested Bold text</b>Nested Normal text</p>Normal text<i>italic text</i></p>')


if __name__ == "__main__":
    unittest.main()