from dl2np.utils import get_path
from unittest.mock import patch, mock_open
import argparse

from dl2np.utils import get_config


def test_get_path():
    out = get_path()
    condition = isinstance(out, str)
    out_str = str(type(out))
    error_str = f"Expected type(out) == str. Received type(out) == {out_str}."
    assert condition, error_str


# Sample config file content with a large string
config_content = """
param1: default_value1
param2: 10
large_text: |
  This is a large string for a language model.
  It includes multiple lines of text,
  which are all preserved exactly as written.
  - This
  - is
  - a
  - list
"""


@patch("builtins.open", new_callable=mock_open, read_data=config_content)
@patch("argparse.ArgumentParser.parse_args")
def test_get_config_default(mock_parse_args, mock_file):
    # Mock command-line arguments
    mock_parse_args.return_value = argparse.Namespace(
        config="config.yaml", param1=None, param2=None, large_text=None
    )

    config = get_config()

    expected_config = {
        "param1": "default_value1",
        "param2": 10,
        "large_text": """This is a large string for a language model.
It includes multiple lines of text,
which are all preserved exactly as written.
- This
- is
- a
- list
""",
    }

    assert config == expected_config


@patch("builtins.open", new_callable=mock_open, read_data=config_content)
@patch("argparse.ArgumentParser.parse_args")
def test_get_config_override(mock_parse_args, mock_file):
    # Mock command-line arguments
    mock_parse_args.return_value = argparse.Namespace(
        config="config.yaml", param1="new_value1", param2=20, large_text="Overridden large text"
    )

    config = get_config()

    expected_config = {"param1": "new_value1", "param2": 20, "large_text": "Overridden large text"}

    assert config == expected_config


@patch("builtins.open", new_callable=mock_open, read_data=config_content)
@patch("argparse.ArgumentParser.parse_args")
def test_get_config_partial_override(mock_parse_args, mock_file):
    # Mock command-line arguments
    mock_parse_args.return_value = argparse.Namespace(
        config="config.yaml", param1="new_value1", param2=None, large_text=None
    )

    config = get_config()

    expected_config = {
        "param1": "new_value1",
        "param2": 10,
        "large_text": """This is a large string for a language model.
It includes multiple lines of text,
which are all preserved exactly as written.
- This
- is
- a
- list
""",
    }

    assert config == expected_config
