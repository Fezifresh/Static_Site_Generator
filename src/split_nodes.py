from textnode import TextNode, TextType

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