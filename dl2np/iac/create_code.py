from dl2np.utils import get_config
from dl2np.user_input_to_code import run


def main():
    config = get_config()
    user_input = config["user_input"]
    output_tag = config["output_tag"]
    model_name = config["model_name"]
    run(
        user_input=user_input,
        output_tag=output_tag,
        model_name=model_name,
    )


if __name__ == "__main__":
    main()
