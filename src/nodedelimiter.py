from textnode import TextNode
from htmlnode import HtmlNode, LeafNode, ParentNode
from enums import TextType
import re

def split_node_delimeter(old_nodes, delimeter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            split_string = node.text.split(delimeter)
            if len(split_string) % 2 == 0:
                raise Exception("Improper markdown syntax")
            for i in range(len(split_string)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_string[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(split_string[i], text_type))
    return new_nodes

def split_node_images(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        text_to_search = node.text
        image_regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
        image_tuples = re.findall(image_regex, text_to_search)
        if image_tuples:
            if isinstance(image_tuples[0], tuple):
                for image in image_tuples:
                    new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            else:
                new_nodes.append(TextNode(image_tuples[0], TextType.IMAGE, image_tuples[1]))
        else:
            new_nodes.append(node)
    return new_nodes        


def split_node_links(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        text_to_search = node.text
        link_regex = r"\(([^\(\)]*)\)\[([^\[\]]*)\]"
        link_tuples = re.findall(link_regex, text_to_search)
        if link_tuples:
            if isinstance(link_tuples[0], tuple) :
                for link in link_tuples:
                    new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            else:
                new_nodes.append(TextNode(link_tuples[0], TextType.LINK, link_tuples[1]))
        else:
            new_nodes.append(node)        
    return new_nodes



def text_to_text_node(text):
    base_node = TextNode(text, TextType.TEXT)
    code_nodes = split_node_delimeter([base_node], '`', TextType.CODE)
    img_nodes = split_node_images(code_nodes)
    link_nodes = split_node_links(img_nodes)
    bold_nodes = split_node_delimeter(link_nodes, "**", TextType.BOLD)
    finished_nodes = split_node_delimeter(bold_nodes, "_", TextType.ITALIC)
    return finished_nodes