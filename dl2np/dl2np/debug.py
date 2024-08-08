from pathlib import Path
from dl2np.utils import get_path, remove_markdown_code_blocks, remove_comments
from dl2np.chatbots import chat


def create_prompt(
    user_input: str,
    code_path_str: str,
    test_path: str,
    test_result_path: str,
) -> str:
    out: str = user_input
    # Code str
    code_path: Path = Path(get_path()).parent / f"{code_path_str}"
    code_str: str = Path(code_path).read_text()
    code_str = remove_comments(code_str)  # Remove comments
    # Test str
    test_path: Path = Path(get_path()).parent / f"{test_path}"
    test_str: str = Path(test_path).read_text()
    test_str = remove_comments(test_str)  # Remove comments
    # Test result str
    test_result_path: Path = Path(get_path()).parent / f"{test_result_path}"
    test_result_str: str = test_result_path.read_text()
    out = out.replace("{{ CODE_HERE }}", code_str)
    out = out.replace("{{ TEST_HERE }}", test_str)
    out = out.replace("{{ TEST_RESULT_HERE }}", test_result_str)
    return out


def run(
    user_input: str,
    code_path: str,
    test_path: str,
    test_result_path: str,
    output_tag: str,
    model_name: str = "gpt-4o-mini",
):
    prompt: str = create_prompt(user_input, code_path, test_path, test_result_path)
    response: str = chat(prompt, model_name=model_name)
    response = remove_markdown_code_blocks(response)
    output_path: Path = Path(get_path()).parent / f"{output_tag}"
    # Create the output directory for the file if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write the response to the output file
    with open(output_path, "w") as file:
        file.write(response)
