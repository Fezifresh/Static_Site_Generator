def extract_title(markdown):
    lines = markdown.split("\n")
    found_heading = False
    for line in lines:
        line = line.strip()
        if line [0:2] == "# ":
            found_heading = True
            title = line[2:].strip()
    if found_heading == False:
        raise Exception ("no title found")
    return title
