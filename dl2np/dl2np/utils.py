from pathlib import Path
import argparse
import yaml

import logging
import logging.config


def get_path() -> str:
    """Get the path of the current file.

    Returns:
        str: The path of the current file.
    """
    return str(Path(__file__).resolve().parent)


def remove_markdown_code_blocks(text: str) -> str:
    """
    Remove the line "```python" from the beginning of a block of text
    and remove "```"" from the end of the block of text`

    Args:
        text (str): The text to remove the markdown code blocks from.

    Returns:
        str: The text with the markdown code blocks removed.
    """
    return text.replace("```python", "").replace("```", "")


# TODO: Generalize this function to remove comments from any language
def remove_comments(text: str) -> str:
    """
    Remove all comments from a block of text.

    Args:
        text (str): The text to remove comments from.

    Returns:
        str: The text with comments removed.
    """
    return "\n".join([line for line in text.split("\n") if not line.strip().startswith("#")])


# Get a configuration dictionary from a YAML file and command-line arguments.
# The command-line arguments take precedence over the configuration file.
def get_config() -> dict:
    """
    Get a configuration dictionary from a YAML file and command-line arguments.
    The command-line arguments take precedence over the configuration file.

    Returns:
        dict: The configuration dictionary.
    """
    # Parse the config file argument first
    initial_parser = argparse.ArgumentParser()
    initial_parser.add_argument("--config", type=str, required=True, help="Path to the config file")
    initial_args = initial_parser.parse_args()
    config_path = initial_args.config

    # Load the configuration file
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    # Create the main parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True, help="Path to the config file")

    # Dynamically add arguments based on config keys
    for key, value in config.items():
        arg_type = type(value)
        if arg_type is str and len(value) > 50:  # Adjust threshold as needed
            arg_type = str  # Ensure large strings are handled as strings
        parser.add_argument(f"--{key}", type=arg_type, help=f"Description for {key}")

    # Parse all arguments
    args = parser.parse_args()
    args_dict = vars(args)  # Convert to dictionary

    # Merge config with command-line arguments, giving precedence to command-line args
    merged_config = {
        **config,
        **{k: v for k, v in args_dict.items() if v is not None and k != "config"},
    }

    return merged_config


# Set up logging with default level (INFO)
def setup_logging(level=logging.INFO):
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
        },
        "handlers": {
            "default": {
                "level": "DEBUG",  # Set to DEBUG to allow all levels
                "formatter": "standard",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
            "file": {
                "level": "DEBUG",  # Set to DEBUG to allow all levels
                "formatter": "standard",
                "class": "logging.FileHandler",
                "filename": "dl2np.log",
                "mode": "a",
            },
        },
        "loggers": {
            "dl2np": {  # root logger for the package
                "handlers": ["default", "file"],
                "level": level,
                "propagate": True,
            }
        },
    }
    logging.config.dictConfig(config)


def get_logger(name):
    return logging.getLogger(name)


# Enable  logging with default level (INFO)
setup_logging()
