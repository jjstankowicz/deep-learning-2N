from enum import Enum


class Models(Enum):
    GPT_4O_MINI = "gpt-4o-mini"
    GPT_4O = "gpt-4o"
    GPT_4_TURBO = "gpt-4-turbo"
    GPT_4 = "gpt-4"
    GPT_35_TURBO = "gpt-35-turbo"


def openai(
    user_input: str,
    model_name: Models = Models.GPT_4O_MINI.value,
    temperature: float = 0.0,
    seed: int = 0,
) -> str:
    """Use the OpenAI API to chat with a model.

    Args:
        user_input (str): The user input.
        model_name (Models, optional): The model to use. Defaults to Models.GPT_4O_MINI.value.
        temperature (float, optional): The temperature. A temperature of 0.0 is deterministic. Defaults to 0.0.
        seed (int, optional): The random seed. Defaults to 0.

    Returns:
        str: _description_
    """
    import os
    from openai import OpenAI

    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model=model_name,
        temperature=temperature,
        seed=seed,
    )

    return chat_completion.choices[0].message.content
