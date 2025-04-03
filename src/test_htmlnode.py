import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import text_node_to_html_node, TextType, TextNode


class TestTextNode(unittest.TestCase):
    def test_null_url(self):
        node = HTMLNode("?", "val", ["props"],{"key": "value"}) 
        self.assertEqual(' key="value"',node.props_to_html())

    def test_not_eq(self):
        node = HTMLNode("This is a text node")
        node2 = HTMLNode("This is is a text node")
        self.assertNotEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_props(self):
        node = LeafNode("p", "Hello, world!",{"key": "value"})
        self.assertEqual(node.to_html(), '<p>Hello, world! key="value"</p>')
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
if __name__ == "__main__":
    unittest.main()
