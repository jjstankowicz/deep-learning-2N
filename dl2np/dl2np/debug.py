from pathlib import Path
from dl2np.utils import get_path, remove_markdown_code_blocks, remove_comments

# from dl2np.chatbots import chat
import subprocess


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


def get_test_result(test_filename: str) -> tuple[bool, str]:
    """Run the pytest on the specified test file and return the result.

    Args:
        test_filename (str): The name of the test file.

    Returns:
        tuple[bool, str]: A tuple containing:
            - A boolean indicating whether the test passed (True) or failed (False)
            - The error output as a string if the test failed, or an empty string if it passed
    """
    result = subprocess.run(["pytest", test_filename, "-v"], capture_output=True, text=True)

    if result.returncode == 0:
        return True, ""
    else:
        return False, result.stdout + result.stderr


def run(
    # user_input: str,
    # code_path: str,
    test_path: str,
    # output_tag: str,
    # model_name: str = "gpt-4o-mini",
):
    failing_test = True
    while failing_test:
        # 1. Get the test result and error message
        test_result, test_result_str = get_test_result(test_path)
        failing_test = not test_result
        breakpoint()
        # if failing_test:
        #     # 2. Modify the code and test
        #     modify_code_and_test(user_input, code_path, test_path, output_tag, model_name)
        # else:
        #     # 3. If the test passed, save the code and test
        #     save_code_and_test(user_input, code_path, test_path, output_tag)
