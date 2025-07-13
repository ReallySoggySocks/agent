import os
import subprocess
import stat

def run_python_file(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    abs_wd = os.path.abspath(working_directory)
    abs_fp = os.path.abspath(full_path)

    if not abs_fp.startswith(abs_wd):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    elif not os.path.exists(abs_fp):
        return f'Error: File "{file_path}" not found'
    elif not abs_fp.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'
    else:
        try:
            output = subprocess.run(args=["python", file_path], cwd=abs_wd, capture_output=True, timeout=30)
            if output.returncode != 0:
                r_code = output.returncode
                return f"Process exited with return code {r_code}"
            elif output.stderr == b'' and output.stdout == b'':
                return "No output produced"
            else:
                return f"STDOUT:{output.stdout.decode()}\nSTDERR:{output.stderr.decode()}"

        except Exception as e:
            return f"Error: {e}"