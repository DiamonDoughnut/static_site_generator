import os
from markdownblocks import markdown_to_html_node


def generate_page(from_path, template_path, dest_path, basepath):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/',f'href="{basepath}')
    template = template.replace('src="/',f'src="{basepath}')

    to_file = open(dest_path, "w")
    to_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):

    if basepath == "":
        basepath == "/"
    
    if not os.path.isdir(dir_path_content):
        print(f"Error: Source directory not found: {dir_path_content}")

    os.makedirs(dest_dir_path, exist_ok=True)

    for item in os.listdir(dir_path_content):
        dir_path_item = os.path.join(dir_path_content, item)
        dst_path_item = os.path.join(dest_dir_path, item)

        if os.path.isdir(dir_path_item):
            generate_pages_recursive(dir_path_item, template_path, dst_path_item, basepath)

        elif os.path.isfile(dir_path_item):
            dst_page_dir = os.path.splitext(dst_path_item)[0]
            dst_page_path = dst_page_dir +".html"

            generate_page(dir_path_item, template_path, dst_page_path, basepath)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")
