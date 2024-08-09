from dl2np.utils import get_config
from dl2np.debug import run


def main():
    config = get_config()
    tag = config["tag"]
    run(tag=tag)


if __name__ == "__main__":
    main()
