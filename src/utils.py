import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    return matches

def split_nodes_image(old_nodes):
    final_list = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            final_list.append(node)
        prop_list = extract_markdown_images(node.text)
        if len(prop_list) == 0:
            final_list.append(node)
            continue
        list = []
        for prop in prop_list:
            new_list = node.text.split(f'![{prop[0]}]({prop[1]})', 1)
            if len(new_list) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if new_list[0] != '':
                list.append(TextNode(new_list[0], text_type_text))
            list.append(TextNode(prop[0],text_type_image, prop[1]))
            node.text = new_list[1]
        if node.text != '':
            list.append(TextNode(node.text, text_type_text))
        final_list.extend(list)
    return final_list

def split_nodes_link(old_nodes):
    final_list = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            final_list.append(node)
        prop_list = extract_markdown_links(node.text)
        if len(prop_list) == 0:
            final_list.append(node)
            continue
        list = []
        for prop in prop_list:
            new_list = node.text.split(f'[{prop[0]}]({prop[1]})', 1)
            if len(new_list) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if new_list[0] != '':
                list.append(TextNode(new_list[0], text_type_text))
            list.append(TextNode(prop[0],text_type_link, prop[1]))
            node.text = new_list[1]
        if node.text != '':
            list.append(TextNode(node.text, text_type_text))
        final_list.extend(list)
    return final_list