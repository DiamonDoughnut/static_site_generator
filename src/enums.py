from enum import Enum

class TextType(Enum):
    TEXT="p"
    BOLD="b"
    ITALIC="i"
    CODE="code"
    LINK="a"
    IMAGE="img"

class BlockType(Enum):
    PARAGRAPH="p"
    HEADING="h1"
    CODE="code"
    QUOTE="quote"
    ULIST="ul"
    OLIST="ol"    