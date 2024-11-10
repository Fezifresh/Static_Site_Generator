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
        front_tag = "<" + self.tag + self.props_to_html() + ">"
        end_tag = "</" + self.tag + ">"
        return front_tag + self.value + end_tag

    def __repr__(self):
        print (f"LEAFNODE(tag = {self.tag}, value = {self.value}, props = {self.props}")
        return