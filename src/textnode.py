from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url = ""):
        self.text= text
        self.text_type = text_type
        if len(url) > 0:
            self.url = url
        else:
            self.url = None

    def __eq__(self, node):
        if self.text == node.text:
            if self.text_type == node.text_type:
                if self.url == node.url:
                    return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

        
def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
            return LeafNode("b",text_node.text)
    elif text_node.text_type == TextType.ITALIC:
            return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
            return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
            return LeafNode("a", text_node.text,{"href":text_node.url})
    elif text_node.text_type == TextType.IMAGE:
            return LeafNode("img", "",{"src":text_node.url,"alt":text_node.text})
