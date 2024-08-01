import pytest
from dl2np.chatbots import openai


def test_openai():
    out = openai("Hello, how are you?")
    condition = isinstance(out, str)
    error_str = "Expected type(out) == str. Received type(out) == {0}.".format(type(out))
    assert condition, error_str
