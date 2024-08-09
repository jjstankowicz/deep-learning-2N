from dl2np.utils import get_config
from dl2np.debug import run


def main():
    config = get_config()
    user_input = config["user_input"]
    tag = config["tag"]
    model_name = config["model_name"]
    run(
        user_input=user_input,
        tag=tag,
        model_name=model_name,
    )


if __name__ == "__main__":
    main()
