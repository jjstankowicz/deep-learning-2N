from pathlib import Path
from dl2np.utils import get_path, remove_markdown_code_blocks
from dl2np.chatbots import chat


def create_prompt(user_input: str, code_path_str: str) -> str:
    out: str = user_input
    code_path: Path = Path(get_path()).parent / f"{code_path_str}"
    code_str: str = Path(code_path).read_text()
    # Remove all comments from the code_str
    code_str = "\n".join(
        [line for line in code_str.split("\n") if not line.strip().startswith("#")]
    )
    return out.replace("{{ CODE_HERE }}", code_str)


def run(user_input: str, code_path: str, output_tag: str, model_name: str = "gpt-4o-mini") -> None:
    prompt: str = create_prompt(user_input, code_path)
    response: str = chat(prompt, model_name=model_name)
    response = remove_markdown_code_blocks(response)
    output_path: Path = Path(get_path()).parent / f"{output_tag}"
    # Create the output directory for the file if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write the response to the output file
    with open(output_path, "w") as file:
        file.write(response)
