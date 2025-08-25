from enums import TextType
from markdownblocks import *
import os
import shutil


def main():
    generate()
    
    
    
def generate():
    public_dir="./public"
    start_dir="./static"

    if not os.path.exists(start_dir):
        print("Error: Static folder must be in the base directory with all contents present")
        return

    if not os.path.exists(public_dir):
        print("Public folder does not exist: it will be created.")
        os.mkdir(public_dir)
    else:
        print("Clearing public folder for clean generation.")
        shutil.rmtree(public_dir)
        os.mkdir(public_dir)    


    print("Folders verified, beginning copy")

    recursive_generation(public_dir, start_dir)



def recursive_generation(public, start):
    contents = os.listdir(start)
    if not contents:
        print("Error: The static folder is empty. No files to copy.")
        return
    for item in contents:
        src_path = os.path.join(start, item)
        dst_path = os.path.join(public, item)

        if os.path.isfile(src_path):
            shutil.copy2(src_path, dst_path)
            print( f"Copied file item '{item}'")
        elif os.path.isdir(src_path):
            os.mkdir(dst_path)
            recursive_generation(dst_path, src_path)
            print(f"Copied directory '{item}'")

            






main()    