import re

def markdown_to_blocks(text):
    lines = text.split("\n\n")
    new_blocks = []
    for line in lines:
        if line != "":
            new_blocks.append(line.strip())
    return new_blocks

def block_to_block_type(markdown_block):
    type = "Normal Text"
    lines = markdown_block.split("\n")
    is_heading = None
    is_quote = None
    is_unordered_list = None
    is_ordered_list = None

    heading_match = re.search(r"^\#+", markdown_block)
    if (heading_match != None) and (len(heading_match.group()) <= 6):
        is_heading = True
        type = "Heading"
        return type

    if markdown_block[0:3] == "```" and markdown_block[-3:] == "```":
        type = "Code"
        return type

    for line in lines:
        if line[0] == ">":
            is_quote = True
        else:
            is_quote = False
            break
    if is_quote == True:
        type = "Quote"
        return type 

    for line in lines:
        if (line[0:2] == "* ") or (line[0:2] == "- "):
            is_unordered_list = True
        else: 
            is_unordered_list = False
            break
    if is_unordered_list == True:
        type = "Unordered List"
        return type
    
    list_of_line_numbers = []
    for line in lines:
        line_number = re.search(r"^\d+\.", line)
        if line_number == None:
            is_ordered_list = False
            break
        list_of_line_numbers.append(int(line_number.group()[:-1]))
    if list_of_line_numbers[0] != 1:
        is_ordered_list = False
    elif is_ordered_list != False:
        for number in list_of_line_numbers:
            if number == len(list_of_line_numbers[0:number]):
                is_ordered_list = True
            else:
                is_ordered_list = False
                break
    if is_ordered_list == True:
        type = "Ordered List"
        return type

    return type