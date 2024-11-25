from textnode import TextNode, TextType
from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node, text_to_children
from htmlnode import HTMLNode, ParentNode, LeafNode
import os
import shutil

source_directory = "/home/fezifresh/workspace/github.com/Fezifresh/Static_Site_Generator/content/"
template_path = "/home/fezifresh/workspace/github.com/Fezifresh/Static_Site_Generator/template.html"
destination_directory = "/home/fezifresh/workspace/github.com/Fezifresh/Static_Site_Generator/public/"

def main():
    copy_content(source_directory, destination_directory)
    generate_pages_recursive(source_directory, template_path, destination_directory)
    #generate_page("/home/fezifresh/workspace/github.com/Fezifresh/Static_Site_Generator/content/index.md", template_path, "/home/fezifresh/workspace/github.com/Fezifresh/Static_Site_Generator/public/index.html")
    return

def copy_content(source, destination):
    path_source = source
    path_destination = destination

    if os.path.exists(path_destination):
        shutil.rmtree(path_destination)
        os.mkdir(path_destination)
    content = os.listdir(path_source)
    
    for file in content:
        if os.path.isfile(path_source + file):
            shutil.copy(path_source + file, path_destination)
        else:
            os.mkdir(destination + file + "/")
            copy_content(path_source + file + "/", path_destination + file + "/")
    return

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f_from:
        from_path_content = f_from.read()
    
    with open(template_path) as f_template:
        template_path_content = f_template.read()
    
    title = extract_title(from_path_content)
    html_content = markdown_to_html_node(from_path_content).to_html()
    updated_template = template_path_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    
    dest_path_name = os.path.dirname(dest_path)
    os.makedirs(dest_path_name, 0o777, True)
    with open(dest_path, "w") as f_dest:
        f_dest.write(updated_template)
    
    return

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content = os.listdir(dir_path_content)
    for entry in content:
        if os.path.isfile(os.path.join(dir_path_content, entry)) and entry[-3:] == ".md":
            generate_page(os.path.join(dir_path_content, entry), template_path, os.path.join(dest_dir_path, entry[:-2] + "html"))
        elif os.path.isdir(os.path.join(dir_path_content, entry)):
            generate_pages_recursive(os.path.join(dir_path_content, entry), template_path, os.path.join(dest_dir_path, entry))
    return

main()