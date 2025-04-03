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
        if self.props is not None:
            return " "+reduce(lambda acc, x: acc + f'{x[0]}="{x[1]}"',self.props.items(),"") 
        else:
            return ""

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {[item for item in self.children]}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag,value,props=props)
    def to_html(self):
        if self.value == None:
            raise ValueError()
        if self.tag == None:
            return str(self.value)
        return f"<{self.tag}>{self.value}{self.props_to_html()}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag,None, children, props)
    def to_html(self):
        if self.tag == None:
            raise ValueError()
        if self.children == None:
            raise ValueError()
        res =f"<{self.tag}>"
        for child in self.children:
            s = child.to_html()
            if s is not None:
                res += s
        res +=f"</{self.tag}>"
        return res

