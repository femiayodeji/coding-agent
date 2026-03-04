import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        working_file_path = os.path.join(working_directory, file_path)
        if not os.path.abspath(working_file_path).startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(working_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not working_file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", working_file_path]
        if args:
            command.extend(args)
        subprocess_result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        output_lines = []
        if subprocess_result.returncode != 0:
            output_lines.append(f"Error: Process exited with code {subprocess_result.returncode}")
        if not subprocess_result.stdout and not subprocess_result.stderr:
            output_lines.append("No output produced")
        if subprocess_result.stdout:
            output_lines.append(f"STDOUT: {subprocess_result.stdout.strip()}")
        if subprocess_result.stderr:
            output_lines.append(f"STDERR: {subprocess_result.stderr.strip()}")

        return "\n".join(output_lines)

    except Exception as e:
        return f"Error: executing Python file: {e}"



schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file relative to the working directory, with optional command-line arguments. Captures and returns the output, error messages, and exit status of the execution.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of command-line arguments to pass to the Python file",
            ),
        },
        required=["file_path"],
    ),
)