import unittest

from markdown_to_html_node import markdown_to_html_node, text_to_children
from htmlnode import HTMLNode, ParentNode, LeafNode

class TestMarkdownToHTMLNode(unittest.TestCase):

    def test_eq(self):
        text = "This is a paragraph of text with a **bold word**"
        compare_node = ParentNode("div", [ParentNode("p", [LeafNode(None, "This is a paragraph of text with a ", None), LeafNode("b", "bold word", None)], None)], None)
        result = markdown_to_html_node(text)
        self.assertEqual(result, compare_node)
        
    def test_eq_2(self):
        text = "# This is a heading"
        compare_node = ParentNode("div", [ParentNode("h1", [LeafNode(None, "This is a heading", None)], None)], None)
        self.assertEqual(markdown_to_html_node(text), compare_node)

    def test_eq_3(self):
        text = "> This is a quote\n> it has two lines"
        compare_node = ParentNode("div", [ParentNode("blockquote", [LeafNode(None, "This is a quote it has two lines", None)], None)], None)
        self.assertEqual(markdown_to_html_node(text), compare_node)

    def test_eq_4(self):
        text = "```\nThis is code\n```"
        compare_node = ParentNode("div", [ParentNode("code", [LeafNode(None, "This is code", None)], None)], None)
        self.assertEqual(markdown_to_html_node(text), compare_node)

    def test_eq_5(self):
        text = "* this is a list\n* this is the second item"
        compare_node = ParentNode("div", [ParentNode("ul", [ParentNode("li", [LeafNode(None, "this is a list", None)], None), ParentNode("li", [LeafNode(None, "this is the second item", None)], None)], None)], None)
        self.assertEqual(markdown_to_html_node(text), compare_node)

    def test_eq_6(self):
        text = "1. this is a list\n2. this is the second item"
        compare_node = ParentNode("div", [ParentNode("ol", [ParentNode("li", [LeafNode(None, "this is a list", None)], None), ParentNode("li", [LeafNode(None, "this is the second item", None)], None)], None)], None)
        self.assertEqual(markdown_to_html_node(text), compare_node)

    def test_eq_7(self):
        text = "* this is a list\n* this is the **second item**"
        compare_node = ParentNode("div", [ParentNode("ul", [ParentNode("li", [LeafNode(None, "this is a list", None)], None), ParentNode("li", [LeafNode(None, "this is the ", None), LeafNode("b", "second item", None)], None)], None)], None)
        self.assertEqual(markdown_to_html_node(text), compare_node)

    def test_eq_8(self):
        text = "## this is a heading\n\n* this is a list\n* this is the **second item**"
        compare_node = ParentNode("div", [ParentNode("h2", [LeafNode(None, "this is a heading", None)], None), ParentNode("ul", [ParentNode("li", [LeafNode(None, "this is a list", None)], None), ParentNode("li", [LeafNode(None, "this is the ", None), LeafNode("b", "second item", None)], None)], None)], None)
        result = markdown_to_html_node(text)
        test = result.to_html()
        print (test)
        self.assertEqual(markdown_to_html_node(text), compare_node)
if __name__ == "__main__":
    unittest.main()