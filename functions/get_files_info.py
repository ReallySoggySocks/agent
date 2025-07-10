import os

def get_files_info(working_directory, directory=None):
    full_path = os.path.join(working_directory, directory)
    abs_wd = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(full_path)

    str_list = []
    if directory == ".":
        str_list.append("Result for current directory:")
    else:
        str_list.append(f"Result for '{directory}' directory:")

    if not abs_full_path.startswith(abs_wd):
        str_list.append(f'  Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return "\n".join(str_list)
    if not os.path.isdir(abs_full_path):
        str_list.append(f'  Error: "{directory}" is not a directory')
        return "\n".join(str_list)
    else:
        for item in os.listdir(full_path):
            item_path = os.path.join(full_path, item)
            str_list.append(f'- {item}: file_size={os.path.getsize(item_path)}, is_dir={os.path.isdir(item_path)}')
        return "\n".join(str_list)
    