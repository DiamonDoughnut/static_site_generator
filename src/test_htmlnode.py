from htmlnode import *
from textnode import TextNode
from enums import TextType

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


if __name__ == "__main__":
    unittest.main()        