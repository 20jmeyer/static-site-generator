from textnode import TextNode, TextType
from htmlnode import HTMLNode
def main():
    node = TextNode("Hello", TextType.BOLD, "http://google.com")
    print(node)
    node2 = HTMLNode("asd", "fgh", ["props"],{"key": "value"})
    print(node2.props_to_html())
    print(node2)

main()
