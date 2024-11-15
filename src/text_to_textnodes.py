from textnode import TextNode, TextType
from split_nodes import split_nodes_delimeter, split_nodes_image, split_nodes_links

def text_to_textnodes(text):
    list_of_nodes = []
    original_node = TextNode(text, TextType.TEXT)
    split_node = split_nodes_links(split_nodes_image(split_nodes_delimeter(split_nodes_delimeter(split_nodes_delimeter([original_node], "**", TextType.BOLD), "*", TextType.ITALIC), "`", TextType.CODE)))
    
    return split_node