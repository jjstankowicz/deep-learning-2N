from pathlib import Path
from dl2np.utils import get_path, remove_markdown_code_blocks
from dl2np.chatbots import openai


def create_prompt(user_input: str, code_path: str) -> str:
    out: str = user_input
    code_str: str = Path(code_path).read_text()
    return out.replace("{{ CODE_HERE }}", code_str)


def run(user_input: str, code_path: str, output_tag: str) -> None:
    prompt: str = create_prompt(user_input, code_path)
    response: str = openai(prompt)
    response = remove_markdown_code_blocks(response)
    output_path: Path = Path(get_path()).parent / f"{output_tag}.py"
    # Create the output directory for the file if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write the response to the output file
    with open(output_path, "w") as file:
        file.write(response)
