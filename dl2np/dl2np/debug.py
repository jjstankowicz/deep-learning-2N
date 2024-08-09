from pathlib import Path
from dl2np.utils import get_path, remove_markdown_code_blocks, remove_comments

# from dl2np.chatbots import chat
import subprocess


class Debugger:
    def __init__(self, tag: str):
        self.tag: str = tag
        self.parse_tag()

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
        out = out.replace("{{ CODE_HERE }}", code_str)
        out = out.replace("{{ TEST_HERE }}", test_str)
        out = out.replace("{{ TEST_RESULT_HERE }}", self.test_result_str)
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

    def modify_code_and_test(self):
        self.set_prompt()

    def run(
        self,
        # user_input: str,
        # code_path: str,
        # model_name: str = "gpt-4o-mini",
    ):
        failing_test = True
        while failing_test:
            # 1. Get the test result and error message
            self.set_test_result()
            test_result = self.test_result["passed"]
            self.test_result_str = self.test_result["error"]
            failing_test = not test_result
            breakpoint()
            # if failing_test:
            #     # 2. Modify the code and test
            #     modify_code_and_test(user_input, code_path, test_path, output_tag, model_name)
            # else:
            #     # 3. If the test passed, save the code and test
            #     save_code_and_test(user_input, code_path, test_path, output_tag)


def run(tag: str, model_name: str = "gpt-4o-mini") -> None:
    debugger = Debugger(tag=tag)
    debugger.run()
