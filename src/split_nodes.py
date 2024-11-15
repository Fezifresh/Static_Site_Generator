from textnode import TextNode, TextType
from extract_links import extract_markdown_images, extract_markdown_links

def split_nodes_delimeter(old_nodes, delimeter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)

        elif node.text.find(delimeter) == -1:
            new_nodes.append(node)
        
        else:    
            first_delimeter_index = node.text.find(delimeter)
            second_delimeter_index = node.text.find(delimeter, first_delimeter_index+1)
            if second_delimeter_index == -1:
                raise Exception(f"no second delimeter for {text_type} found")
            
            split_node = []
            if first_delimeter_index != 0:
                split_node.append(TextNode(node.text[:first_delimeter_index], TextType.TEXT))
            first_delimeter_index += len(delimeter) -1 
            split_node.append(TextNode(node.text[first_delimeter_index+1:second_delimeter_index], text_type))
            second_delimeter_index += len(delimeter) -1 
            if len(node.text[second_delimeter_index+1:]) != 0:
                if delimeter in node.text[second_delimeter_index+1:]:
                    new_list = [TextNode(node.text[second_delimeter_index+1:], TextType.TEXT)]
                    split_node.extend(split_nodes_delimeter(new_list, delimeter, text_type))
                else:
                    split_node.append(TextNode(node.text[second_delimeter_index+1:], TextType.TEXT))      
            new_nodes.extend(split_node)

    return new_nodes

#TextNode(obi wan image, image text, https://i.imgur.com/fJRm4Vk.jpeg)

def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if extract_markdown_links(node.text) == []:
            new_nodes.append(node)
        else:
            matches = extract_markdown_links(node.text)
            text = node.text
            split_node = []
            for match in matches:
                split_node.append(TextNode(text.split(f"[{match[0]}]({match[1]})", 1)[0], node.text_type))
                split_node.append(TextNode(match[0], TextType.LINK, match[1]))
                text = text.split(f"[{match[0]}]({match[1]})", 1)[1]
            split_node.append(TextNode(text, node.text_type))
            for node in split_node:
                if node.text != "":
                    new_nodes.append(node)

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if extract_markdown_images(node.text) == []:
            new_nodes.append(node)
        else:
            matches = extract_markdown_images(node.text)
            text = node.text
            split_node = []
            for match in matches:
                split_node.append(TextNode(text.split(f"![{match[0]}]({match[1]})", 1)[0], node.text_type))
                split_node.append(TextNode(match[0], TextType.IMAGE, match[1]))
                text = text.split(f"![{match[0]}]({match[1]})", 1)[1]
            split_node.append(TextNode(text, node.text_type))
            for node in split_node:
                if node.text != "":
                    new_nodes.append(node)
    
    return new_nodes