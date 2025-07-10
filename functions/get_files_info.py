import os

def get_files_info(working_directory, directory=None):
    full_path = os.path.join(working_directory, directory)
    if working_directory not in os.path.abspath(full_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    else:
        print(os.listdir(full_path))
        str_list = []
        for file in os.listdir(full_path):
            str_list.append(f'- {file}: file_size={os.path.getsize(file)}, is_dir={os.path.isdir(file)}')

        return "\n".join(str_list)
    