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
    HEADING1="h1"
    HEADING2="h2"
    HEADING3="h3"
    HEADING4="h4"
    HEADING5="h5"
    HEADING6="h6"
    CODE="code"
    QUOTE="quote"
    ULIST="ul"
    OLIST="ol"    