from dl2np.utils import get_config
from dl2np.code_to_unittest import run


def main():
    config = get_config()
    user_input = config["user_input"]
    code_path = config["code_path"]
    output_tag = config["output_tag"]
    model_name = config["model_name"]
    run(
        user_input=user_input,
        code_path=code_path,
        output_tag=output_tag,
        model_name=model_name,
    )


if __name__ == "__main__":
    main()
