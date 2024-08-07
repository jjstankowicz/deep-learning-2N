import pytest
from typing import Any
from dl2np.chatbots import chat

MODEL_NAMES = ["gpt-4o-mini", "claude-3-haiku-20240307"]


def _check_str(out: Any) -> None:
    condition = isinstance(out, str)
    error_str = f"Expected type(out) == str. Received type(out) == {type(out)}."
    assert condition, error_str


@pytest.mark.parametrize("model_name", MODEL_NAMES)
def test_chat(model_name: str):
    out = chat("Hello, how are you?", model_name=model_name)
    _check_str(out)
