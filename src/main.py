from enums import TextType
from markdownblocks import *

md = """# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""

def main():
    test = markdown_to_html_node(md)
    print(f"top_level: {test.tag}")
    for node in test.children:
        print(f"second_level: {node.tag}")
        if node.children:
            for node_down in node.children:
                print(f"third_level: {node.tag}")
    



main()    