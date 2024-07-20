import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_print(self):
        node1 = HTMLNode('p', 'Just a test para')
        node2 = HTMLNode('p', 'Just a test para')
        self.assertEqual(print(node1), print(node2))
    
    def test_eq(self):
        node1 = HTMLNode('b','This is bold text')
        node2 = HTMLNode('b','This is bold text')
        self.assertEqual(node1,node2)
    
    def test_props(self):
        node = HTMLNode('input',None,None,{'type':'text', 'maxlength':'50'})
        expected = ' type="text" maxlength="50"'
        self.assertEqual(node.props_to_html(), expected)
    
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, None, {'class': 'primary'})",
        )

if __name__ == '__main__':
    unittest.main()