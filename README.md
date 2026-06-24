# Coding Agent

A small command-line coding agent powered by Gemini. It can inspect the local workspace, read and write files, and run Python files through a limited tool interface. The agent is designed to work inside a sandboxed working directory so file access stays controlled.

The repository also includes a simple calculator example under `calculator/` that the agent can use as a target workspace.

## Setup

1. Make sure you have Python 3.13 or newer.
2. Create and activate a virtual environment:

	```bash
	python -m venv .venv
	source .venv/bin/activate
	```

3. Install the dependencies:

	```bash
	pip install google-genai==1.12.1 python-dotenv==1.1.0
	```

4. Create a `.env` file in the project root and add your Gemini API key:

	```bash
	GEMINI_API_KEY=your_api_key_here
	```

## Run

Use the CLI with a prompt:

```bash
python main.py "List the files in the calculator project"
```

Add `--verbose` to see token usage and tool calls:

```bash
python main.py "Read calculator/main.py" --verbose
```

## Concepts

- Tool calling: the agent can call file and execution helpers instead of guessing.
- Workspace sandboxing: file access is restricted to the working directory.
- File inspection: list directories and read file contents.
- File editing: write or overwrite files when needed.
- Python execution: run Python files and capture output.
- Example app: the `calculator/` folder shows a small runnable Python project.

## Project Layout

- `main.py`: CLI entry point that sends prompts to Gemini.
- `prompt.py`: system instructions for the agent.
- `functions/`: tool implementations used by the model.
- `calculator/`: sample workspace and calculator example.

