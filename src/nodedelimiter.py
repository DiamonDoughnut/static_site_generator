from textnode import *
from htmlnode import *
import re

def split_node_delimeter(old_nodes, delimeter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            split_string = delimeter.split(node.text)
            if len(split_string) % 2 == 0:
                raise Exception("Improper markdown syntax")
            for i in range(len(split_string)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_string[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(split_string[i], text_type))
    return new_nodes

def extract_markdown_images(text):
    image_regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    image_tuples = re.findall(image_regex, text)
    return image_tuples

def extract_markdown_links(text):
    link_regex = r"\(([^\(\)]*)\)\[([^\[\]]*)\]"
    link_tuples = re.findall(link_regex, text)
    return link_tuples
