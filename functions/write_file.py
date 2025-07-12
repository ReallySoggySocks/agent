import os

def write_file(working_diretory, file_path, content):
    full_path = os.path.join(working_diretory, file_path)
    abs_wd = os.path.abspath(working_diretory)
    abs_fp = os.path.abspath(full_path)

    if not abs_fp.startswith(abs_wd):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        with open(abs_fp, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"