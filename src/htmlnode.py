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
        print (f"HTMLNODE(tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props}")
        return
    
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
        print (f"LEAFNODE(tag = {self.tag}, value = {self.value}, props = {self.props}")
        return
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("All parent nodes must have a tag")
        if self.children == None:
            raise ValueError("All parent nodes must have children")
        if isinstance(self, LeafNode):
            print("I am a leaf")
            return self.to_html()
        return f"<{self.tag}{self.props_to_html()}>{''.join(list(map(methodcaller('to_html'), self.children)))}</{self.tag}>"
    
    def __repr__(self):
        print (f"PARENTNODE(tag = {self.tag}, children = {self.children}, props = {self.props}")
        return