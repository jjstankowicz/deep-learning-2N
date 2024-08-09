from pathlib import Path
from dl2np.utils import get_path, remove_markdown_code_blocks, remove_comments
from dl2np.chatbots import chat

# from dl2np.chatbots import chat
import subprocess


class Debugger:
    def __init__(self, tag: str, model_name: str) -> None:
        self.tag: str = tag
        self.parse_tag()
        self.model_name: str = model_name
        self.divider_string = "----------"

    def parse_tag(self) -> None:
        self.tag_str: str = self.tag
        self.tag_full: Path = Path(get_path()).parent / f"{self.tag}"
        self.tag_name: str = self.tag_full.name
        self.tag_parent: Path = self.tag_full.parent
        self.code_filename = self.tag_full.with_suffix(".py")
        self.test_filename = self.tag_parent / f"test_{self.tag_name}"
        self.test_filename = self.test_filename.with_suffix(".py")

    def _check_attributes(self) -> None:
        if not hasattr(self, "user_input"):
            raise AttributeError("Please set the user_input attribute before calling this method.")
        if not hasattr(self, "test_filename"):
            raise AttributeError(
                "Please set the test_filename attribute before calling this method."
            )
        if not hasattr(self, "test_result_str"):
            raise AttributeError(
                "Please set the test_result_str attribute before calling this method."
            )

    def set_prompt(self) -> None:
        self._check_attributes()
        out: str = self.user_input
        # Code str
        code_path: Path = Path(get_path()).parent / self.code_filename
        code_str: str = Path(code_path).read_text()
        self.code_str = remove_comments(code_str)  # Remove comments
        # Test str
        test_path: Path = Path(get_path()).parent / self.test_filename
        test_str: str = Path(test_path).read_text()
        self.test_str = remove_comments(test_str)  # Remove comments
        out = out.replace("{{ DIVIDER_STRING }}", self.divider_string)
        out = out.replace("{{ CODE_TEXT }}", self.code_str)
        out = out.replace("{{ TEST_TEXT }}", self.test_str)
        out = out.replace("{{ TEST_RESULT_TEXT }}", self.test_result_str)
        self.prompt = out

    def set_test_result(self) -> None:
        """Run the pytest on the specified test file and return the result.

        Args:
            test_filename (str): The name of the test file.

        Returns:
            tuple[bool, str]: A tuple containing:
                - A boolean indicating whether the test passed (True) or failed (False)
                - The error output as a string if the test failed, or an empty string if it passed
        """
        result = subprocess.run(
            ["pytest", self.test_filename, "-v"], capture_output=True, text=True
        )

        if result.returncode == 0:
            self.test_result = {"passed": True, "error": ""}
        else:
            self.test_result = {"passed": False, "error": result.stdout + result.stderr}

    def update_code_and_test(self) -> None:
        """Update the code and test files with the response from the chatbot."""
        _, scratch, code, test = self.response.split(self.divider_string)
        self.scratch = scratch
        self.code_str = remove_markdown_code_blocks(code)
        self.test_str = remove_markdown_code_blocks(test)
        breakpoint()

    def modify_code_and_test(self):
        self.set_prompt()
        self.response = chat(self.prompt, model_name=self.model_name)
        self.update_code_and_test()

    def run(
        self,
        user_input: str,
    ):
        self.user_input = user_input
        failing_test = True
        while failing_test:
            # 1. Get the test result and error message
            self.set_test_result()
            test_result = self.test_result["passed"]
            self.test_result_str = self.test_result["error"]
            failing_test = not test_result
            if failing_test:
                # 2. Modify the code and test
                self.modify_code_and_test()
                breakpoint()
            # else:
            #     # 3. If the test passed, save the code and test
            #     save_code_and_test(user_input, code_path, test_path, output_tag)


def run(user_input: str, tag: str, model_name: str = "gpt-4o-mini") -> str:
    debugger = Debugger(tag=tag, model_name=model_name)
    debugger.run(user_input=user_input)
    response = debugger.response
    breakpoint()
    return response
