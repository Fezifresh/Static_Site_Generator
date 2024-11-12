import unittest
from split_nodes import split_nodes_delimeter
from textnode import TextNode, TextType

class TestSplitNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        self.assertEqual(split_nodes_delimeter([node], "`", TextType.CODE), [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),
])
    def test_eq_2(self):
        node = TextNode("This is text with a *italic* word", TextType.TEXT)
        self.assertEqual(split_nodes_delimeter([node], "*", TextType.ITALIC), [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word", TextType.TEXT),
])
    def test_eq_3(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        self.assertEqual(split_nodes_delimeter([node], "**", TextType.BOLD), [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("bold", TextType.BOLD),
    TextNode(" word", TextType.TEXT),
])
    def test_eq_4(self):
        node = TextNode("*Italic beginning* we have here", TextType.TEXT)
        self.assertEqual(split_nodes_delimeter([node], "*", TextType.ITALIC), [
    TextNode("Italic beginning", TextType.ITALIC),
    TextNode(" we have here", TextType.TEXT),
])
    def test_eq_5(self):
        node = TextNode("This is text with a **bold ending**", TextType.TEXT)
        self.assertEqual(split_nodes_delimeter([node], "**", TextType.BOLD), [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("bold ending", TextType.BOLD),
])
    def test_eq_6(self):
        node = TextNode("This is text with a **bold** word and **another one**", TextType.TEXT)
        self.assertEqual(split_nodes_delimeter([node], "**", TextType.BOLD), [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("bold", TextType.BOLD),
    TextNode(" word and ", TextType.TEXT),
    TextNode("another one", TextType.BOLD),
])
    def test_eq_7(self):
        node = TextNode("This is text with a **bold** word and **another one** and even **more**", TextType.TEXT)
        self.assertEqual(split_nodes_delimeter([node], "**", TextType.BOLD), [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("bold", TextType.BOLD),
    TextNode(" word and ", TextType.TEXT),
    TextNode("another one", TextType.BOLD),
    TextNode(" and even ", TextType.TEXT),
    TextNode("more", TextType.BOLD),
])   
    def test_eq_8(self):
        node = TextNode("This is text with a **bold** and *italic* word", TextType.TEXT)
        self.assertEqual(split_nodes_delimeter([node], "**", TextType.BOLD), [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("bold", TextType.BOLD),
    TextNode(" and *italic* word", TextType.TEXT),
])
    def test_eq_9(self):
        node = TextNode("This is text with a **bold ending**", TextType.TEXT)
        node2 = TextNode("This is text with a `code block` word", TextType.TEXT)
        self.assertEqual(split_nodes_delimeter([node, node2], "**", TextType.BOLD), [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("bold ending", TextType.BOLD),
    TextNode("This is text with a `code block` word", TextType.TEXT),
])
        
    def test_eq_10(self):
        node = TextNode("This is text with a **bold** and *italic* word", TextType.TEXT)
        self.assertEqual(split_nodes_delimeter(split_nodes_delimeter([node], "**", TextType.BOLD), "*", TextType.ITALIC), [
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("bold", TextType.BOLD),
    TextNode(" and ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC), 
    TextNode(" word", TextType.TEXT),
])

if __name__ == "__main__":
    unittest.main()