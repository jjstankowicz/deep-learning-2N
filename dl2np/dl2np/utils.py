from pathlib import Path
import argparse
import yaml


# Get the path of the current file
def get_path() -> str:
    return str(Path(__file__).resolve().parent)


def get_config():
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
