def markdown_to_blocks(text):
    lines = text.split("\n\n")
    new_lines = []
    for line in lines:
        if line != "":
            new_lines.append(line.strip())
    return new_lines