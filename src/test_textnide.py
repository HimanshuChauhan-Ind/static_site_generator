import unittest

from textnode import TextNode

class TextTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node","bold")
        node1 = TextNode("This is a text node","bold")
        self.assertEqual(node,node1)

    def test_type_not_eq(self):
        node = TextNode("This is a text node","bold")
        node1 = TextNode("This is a text node","small")
        self.assertNotEqual(node,node1)
    
    def test_url_eq(self):
        node = TextNode('this is test','bold',None)
        node1 = TextNode('this is test','bold')
        self.assertEqual(node,node1)

if __name__ == '__main__':
    unittest.main()