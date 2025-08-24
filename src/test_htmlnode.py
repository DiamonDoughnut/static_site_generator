import unittest

from htmlnode import *
from textnode import *
from main import *

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):

        test_cases = [
            ["a", "text", [], {"href": "styles.css", "class": "section"}, '<tag=a value=text children=[], props= href="styles.css" class="section" >', self.assertEqual],
            ["a", "text", [], {}, '<tag=a value=text2 children=, props=>', self.assertNotEqual],
            ["a", "text", [], {"href": "styles.css", "class": "section"}, '<tag=a value=text children=, props=>', self.assertNotEqual],
        ]

        for case in test_cases:
            test_obj = HtmlNode(case[0], case[1], case[2], case[3])
            test_prnt = f"{test_obj}"
            case[5](case[4], test_prnt)

        leaf_test_cases = [
            ["p", "Hello World", None, "<p>Hello World</p>", self.assertEqual],
            ["a", "Click Me!", {"href": "https://www.google.com"}, '<a href="https://www.google.com" >Click Me!</a>', self.assertEqual],
            ["span", "This should fail", None, "<span>Because this is different</span>", self.assertNotEqual]
        ]    

        for case in leaf_test_cases:
            test_obj = LeafNode(case[0], case[1], case[2])
            case[4](test_obj.to_html(), case[3])


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

    def test_to_html_with_multiples(self):
        grandchild_node_one_one = LeafNode("p", "child 1-1")        
        grandchild_node_one_two = LeafNode("p", "child 1-2")        
        child_node_one = ParentNode("span", [grandchild_node_one_one, grandchild_node_one_two])
        grandchild_node_two_one = LeafNode("p", "child 2-1")        
        child_node_two = ParentNode("span", [grandchild_node_two_one])        
        grandchild_node_three_one = LeafNode("p", "child 3-1")        
        grandchild_node_three_two = LeafNode("p", "child 3-2")        
        grandchild_node_three_three = LeafNode("p", "child 3-3")        
        grandchild_node_three_four = LeafNode("p", "child 3-4")        
        child_node_three = ParentNode("span", [grandchild_node_three_one, grandchild_node_three_two, grandchild_node_three_three, grandchild_node_three_four])        
        grandchild_node_four_one = LeafNode("p", "child 4-1")        
        grandchild_node_four_two = LeafNode("p", "child 4-2")        
        child_node_four = ParentNode("span", [grandchild_node_four_one, grandchild_node_four_two])        
        grandchild_node_five_one = LeafNode("p", "child 5-1")        
        child_node_five = ParentNode("span", [grandchild_node_five_one])        
        grandparent_node = ParentNode("div", [child_node_one, child_node_two, child_node_three, child_node_four, child_node_five])
        self.assertEqual(
            grandparent_node.to_html(),
            "<div><span><p>child 1-1</p><p>child 1-2</p></span><span><p>child 2-1</p></span><span><p>child 3-1</p><p>child 3-2</p><p>child 3-3</p><p>child 3-4</p></span><span><p>child 4-1</p><p>child 4-2</p></span><span><p>child 5-1</p></span></div>",
        ) 



    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")    


if __name__ == "__main__":
    unittest.main()        