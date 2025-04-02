from textnode import TextNode, TextType
def main():
    node = TextNode("Hello", TextType.BOLD, "http://google.com")
    print(node)

main()
