from operator import methodcaller

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        props_string = " "
        if self.props is None:
            return ""
        for key in self.props:
            string = f"{key}=\"{self.props[key]}\""
            props_string += string + " "
        return props_string[0:-1]
    
    def __repr__(self):
        return (f"HTMLNODE(tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props})")
    
    def __eq__(self, other_html_node):
        if self.tag == other_html_node.tag and self.value == other_html_node.value and self.children == other_html_node.children and self.props == other_html_node.props:
            return True
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return (f"LEAFNODE(tag = {self.tag}, value = {self.value}, props = {self.props})")
        
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("All parent nodes must have a tag")
        if self.children == None:
            raise ValueError("All parent nodes must have children")
        if isinstance(self, LeafNode):
            return self.to_html()
        return f"<{self.tag}{self.props_to_html()}>{''.join(list(map(methodcaller('to_html'), self.children)))}</{self.tag}>"
    
    def __repr__(self):
        return (f"PARENTNODE(tag = {self.tag}, children = {self.children}, props = {self.props})")
