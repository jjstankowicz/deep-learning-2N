from pathlib import Path
from dl2np.utils import get_path, remove_markdown_code_blocks
from dl2np.chatbots import chat


def run(user_input: str, output_tag: str, model_name: str = "gpt-4o") -> None:
    response = chat(user_input=user_input, model_name=model_name)
    response = remove_markdown_code_blocks(response)
    output_path = Path(get_path()).parent / f"{output_tag}.py"
    # Create the output directory for the file if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write the response to the output file
    with open(output_path, "w") as file:
        file.write(response)
