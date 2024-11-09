class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_string = " "
        if isinstance(self.props, dict):
            for key in self.props:
                string = f"{key}=\"{self.props[key]}\""
                props_string += string + " "
        return props_string[0:-1]
    
    def __repr__(self):
        print (f"tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props}")
        return