import os

def get_files_info(working_directory, directory=None):
    full_path = os.path.join(working_directory, directory)
    abs_wd = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(full_path)

    if not abs_full_path.startswith(abs_wd):
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if not os.path.isdir(abs_full_path):
        print(f'Error: "{directory}" is not a directory')
    else:
        try:
            str_list = []
            for item in os.listdir(full_path):
                item_path = os.path.join(full_path, item)
                str_list.append(f'- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}')
            return "\n".join(str_list)
    
        except Exception as e:
            return f"Error: {e}"