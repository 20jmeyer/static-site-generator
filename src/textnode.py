from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url):
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

        
