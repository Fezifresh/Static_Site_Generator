from markdown_to_blocks import markdown_to_blocks, block_to_block_type, get_prepared_block, BlockType
from htmlnode import HTMLNode, ParentNode, LeafNode
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    HTML_Nodes = []
    for block in blocks:
        prepared_block, block_type, level = get_prepared_block(block)
        
        match block_type:
            case BlockType.TEXT:
                new_html_node = ParentNode("p", text_to_children(prepared_block, block_type))
                
            case BlockType.HEADING:
                new_html_node = ParentNode(f"h{level}", text_to_children(prepared_block, block_type))
                
            case BlockType.CODE:
                new_html_node = ParentNode("code", text_to_children(prepared_block, block_type))
                
            case BlockType.QUOTE:
                new_html_node = ParentNode("blockquote", text_to_children(prepared_block, block_type))
                
            case BlockType.UNORDERED:
                new_html_node = ParentNode("ul", text_to_children(prepared_block, block_type))
                
            case BlockType.ORDERED:
                new_html_node = ParentNode("ol", text_to_children(prepared_block, block_type))
                
            case _:
                raise Exception ("invalid block type")
        
        HTML_Nodes.append(new_html_node)
    parent_html_node = ParentNode("div", HTML_Nodes)
    
    return parent_html_node

def text_to_children(block, block_type):
    list_of_children = []
    match block_type:
        case BlockType.UNORDERED:
            lines = block.split("\n")
            list_nodes = []
            for line in lines:
                html_textnodes = []    
                textnodes = text_to_textnodes(line)
                for node in textnodes:
                    html_node = text_node_to_html_node(node)
                    html_textnodes.append(html_node)
                list_node = ParentNode("li", html_textnodes)
                list_nodes.append(list_node)
            return list_nodes
        
        case BlockType.ORDERED:
            lines = block.split("\n")
            list_nodes = []
            for line in lines:
                html_textnodes = []    
                textnodes = text_to_textnodes(line)
                for node in textnodes:
                    html_node = text_node_to_html_node(node)
                    html_textnodes.append(html_node)
                list_node = ParentNode("li", html_textnodes)
                list_nodes.append(list_node)
            return list_nodes
        
        case _:
            textnodes = text_to_textnodes(block)
            for node in textnodes:
                html_node = text_node_to_html_node(node)
                list_of_children.append(html_node)
 
    return list_of_children