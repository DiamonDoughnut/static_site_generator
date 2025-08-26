from textnode import TextNode
from enums import TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):

        test_cases = [
            [TextNode("This is a text node", TextType.BOLD), TextNode("This is a text node", TextType.BOLD), self.assertEqual],
            [TextNode("This is a text node", TextType.BOLD), TextNode("This is a different text node", TextType.BOLD), self.assertNotEqual],
            [TextNode("This is a text node", TextType.BOLD), TextNode("This is a text node", TextType.TEXT), self.assertNotEqual],
            [TextNode("This is a text node", TextType.BOLD, None), TextNode("This is a text node", TextType.BOLD, None), self.assertEqual],
            [TextNode("This is a text node", TextType.BOLD, ""), TextNode("This is a text node", TextType.BOLD), self.assertNotEqual],
            [TextNode("This is a text node", TextType.BOLD, 'blank_link'), TextNode("This is a text node", TextType.BOLD, 'blank_link'), self.assertEqual]
        ]

        for case in test_cases:
            case[2](case[0], case[1])
        
    


if __name__ == "__main__":
    unittest.main()