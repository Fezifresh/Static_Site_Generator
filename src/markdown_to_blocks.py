import re
from enum import Enum

class BlockType(Enum):
    TEXT = "normal text block"
    HEADING = "heading block"
    CODE = "code block"
    QUOTE = "quote block"
    UNORDERED = "unordered list block"
    ORDERED = "ordered list block"


def markdown_to_blocks(text):
    lines = text.split("\n\n")
    new_blocks = []
    for line in lines:
        if line != "":
            new_blocks.append(line.strip())
    return new_blocks

def block_to_block_type(markdown_block):
    lines = markdown_block.split("\n")

    heading_match = re.search(r"^\#+", markdown_block)
    if (heading_match != None) and (len(heading_match.group()) <= 6):
        return BlockType.HEADING

    if markdown_block[0:3] == "```" and markdown_block[-3:] == "```":
        return BlockType.CODE

    for line in lines:
        if (line[0:2] == "> "):
            is_quote = True
        else: 
            is_quote = False
            break
    if is_quote == True:
        return BlockType.QUOTE    

    for line in lines:
        if (line[0:2] == "* ") or (line[0:2] == "- "):
            is_unordered_list = True
        else: 
            is_unordered_list = False
            break
    if is_unordered_list == True:
        return BlockType.UNORDERED
    
    list_of_line_numbers = []
    for line in lines:
        line_number = re.search(r"^\d+\.", line)
        if line_number == None:
            is_ordered_list = False
            break
        list_of_line_numbers.append(int(line_number.group()[:-1]))
    for number in list_of_line_numbers:
        if number == len(list_of_line_numbers[0:number]):
            is_ordered_list = True
        else:
            is_ordered_list = False
            break
    if is_ordered_list == True:
        return BlockType.ORDERED
    
    return BlockType.TEXT

def get_prepared_block(markdown_block):
    level = 0
    prepared_block = ""
    block_type = block_to_block_type(markdown_block)
    match block_type:
        case BlockType.TEXT:
            lines = markdown_block.split("\n")
            new_lines = []
            for line in lines:
                new_lines.append(line)
            prepared_block = " ".join(new_lines)
        case BlockType.HEADING:
            heading_match = re.search(r"^\#+", markdown_block)
            level = len(heading_match.group())
            prepared_block = markdown_block [len(heading_match.group())+1:]
        case BlockType.CODE:
            prepared_block = markdown_block[4:-4]
        case BlockType.QUOTE:
            lines = markdown_block.split("\n")
            new_lines = []
            for line in lines:
                new_line = line[2:]
                new_lines.append(new_line)
            prepared_block = " ".join(new_lines)
        case BlockType.UNORDERED:
            lines = markdown_block.split("\n")
            new_lines = []
            for line in lines:
                new_line = line[2:]
                new_lines.append(new_line)
            prepared_block = "\n".join(new_lines)
        case BlockType.ORDERED:
            lines = markdown_block.split("\n")
            new_lines = []
            for line in lines:
                new_line = line[3:]
                new_lines.append(new_line)
            prepared_block = "\n".join(new_lines)
        case _:
            raise Exception ("invalid block type")
    return (prepared_block, block_type, level)
