import pytest
from typing import Any, List
from dl2np.chatbots import openai, anthropic, chat

MODEL_NAMES = ["gpt-4o-mini", "claude-3-haiku-20240307"]

def _check_str(out: Any) -> bool:
    condition = isinstance(out, str)
    error_str = f"Expected type(out) == str. Received type(out) == {type(out)}."
    assert condition, error_str

def test_openai():
    out = openai("Hello, how are you?")
    _check_str(out)

def test_claude():
    out = anthropic("Hello, how are you?")
    _check_str(out)

@pytest.mark.parametrize("model_name", MODEL_NAMES)
def test_chat(model_name: str):
    out = chat("Hello, how are you?", model_name=model_name)
    _check_str(out)