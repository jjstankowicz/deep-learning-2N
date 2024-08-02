from pathlib import Path


# Get the path of the current file
def get_path() -> str:
    return str(Path(__file__).resolve().parent)
