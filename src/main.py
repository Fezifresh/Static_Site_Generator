from textnode import TextNode, TextType
import os
import shutil

source_directory = "/home/fezifresh/workspace/github.com/Fezifresh/Static_Site_Generator/static/"
destination_directory = "/home/fezifresh/workspace/github.com/Fezifresh/Static_Site_Generator/public/"

def main():
    new_text_node = TextNode("hello world", TextType.BOLD, "www.textnode.com")
    print (new_text_node)
    copy_content(source_directory, destination_directory)
    return

def copy_content(source, destination):
    path_source = source
    path_destination = destination
    if os.path.exists(path_destination):
        shutil.rmtree(path_destination)
        os.mkdir(path_destination)
    content = os.listdir(path_source)
    print(f"changing directory\n...\nthis is the content: {content}")
    for file in content:
        if os.path.isfile(path_source + file):
            print(f"{file} is a file!\n...\ncreate a copy of {file}")
            shutil.copy(path_source + file, path_destination)
        else:
            print(f"{file} is a directory!\n...")
            os.mkdir(destination + file + "/")
            print(f"create directory: {file}/")
            copy_content(path_source + file + "/", path_destination + file + "/")
    return

main()