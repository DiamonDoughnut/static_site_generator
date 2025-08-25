from enums import TextType
from markdownblocks import *

md = """# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""

def main():
    blocks = markdown_to_blocks(md)
    print(blocks)
    types = []
    for block in blocks:
        types.append(block_to_block_type(block))
    print(types)    



main()    