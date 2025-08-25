from enums import BlockType

def markdown_to_blocks(text):
    result = []
    split_text = text.split("\n\n")
    for block in split_text:
        result.append(block.strip())
    return result

def block_to_block_type(text):
    if text[0] == "#":
        if text[1] == " ":
            return BlockType.HEADING
    if text[:3] == "```" and text[-3:] == "```":
        return BlockType.CODE
    if text[0] == ">":
        split_by_line = text.split("\n")
        for line in split_by_line:
            if line[0] != ">":
                return BlockType.PARAGRAPH
        return BlockType.QUOTE        
    if text[0] == "-":                           
        split_by_line = text.split("\n")
        for line in split_by_line:
            if line[0] != '-':
                return BlockType.PARAGRAPH
        return BlockType.ULIST        
    if text[0] == "1" and text[1] == ".":
        next = 2
        split_by_line = text.split("\n")
        for line in split_by_line:
            if line[0] != str(next):
                return BlockType.PARAGRAPH
            if line[1] != ".":
                return BlockType.PARAGRAPH
            next += 1             
        return BlockType.OLIST    
    return BlockType.PARAGRAPH    