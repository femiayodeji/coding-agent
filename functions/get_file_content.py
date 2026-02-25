import os

from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        working_file_path = os.path.join(working_directory, file_path)
        if not os.path.abspath(working_file_path).startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(working_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(working_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'        
        return file_content_string
    except Exception as e:
        return f'Error: {str(e)}'