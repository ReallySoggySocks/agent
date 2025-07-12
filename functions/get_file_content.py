import os
from functions.config import MAX_CHARS

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    abs_wd = os.path.abspath(working_directory)
    abs_fp = os.path.abspath(full_path)

    if not abs_fp.startswith(abs_wd):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted directory'
    elif not os.path.isfile(abs_fp):
        return f'Error: File not found or is not a regular file: {file_path}'
    else:
        try:
            with open(abs_fp, "r") as f:
                file_content = f.read(MAX_CHARS)
                char_counter = 0
                for char in f.read():
                    char_counter += 1
                if char_counter > MAX_CHARS:
                    file_content += f'\n[...File "{file_path}" truncated at 10000 characters]'
    
            return file_content
    
        except Exception as e:
            return f"Error:{e}"