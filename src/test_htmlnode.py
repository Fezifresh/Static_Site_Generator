import unittest

from htmlnode import HTMLNode


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

if __name__ == "__main__":
    unittest.main()