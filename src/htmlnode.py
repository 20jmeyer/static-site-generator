from functools import reduce
class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        return reduce(lambda acc, x: acc + f'{x[0]}="{x[1]}"',self.props.items(),"") 

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {[item for item in self.children]}, {self.props})"



