import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_null_url(self):
        node = HTMLNode("?", "val", ["props"],{"key": "value"}) 
        self.assertEqual('key="value"',node.props_to_html())

    def test_not_eq(self):
        node = HTMLNode("This is a text node")
        node2 = HTMLNode("This is is a text node")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
