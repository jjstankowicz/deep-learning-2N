import os
from typing import Union
from enum import Enum
from openai import OpenAI
from anthropic import Anthropic


class OpenAIModels(Enum):
    GPT_4O_MINI = "gpt-4o-mini"
    GPT_4O = "gpt-4o"
    GPT_4_TURBO = "gpt-4-turbo"
    GPT_4 = "gpt-4"
    GPT_35_TURBO = "gpt-35-turbo"


class ClaudeModels(Enum):
    CLAUDE_3_OPUS = "claude-3-opus-20240229"
    CLAUDE_3_SONNET = "claude-3-sonnet-20240229"
    CLAUDE_3_HAIKU = "claude-3-haiku-20240307"


def openai(
    user_input: str,
    model_name: Union[OpenAIModels, str] = OpenAIModels.GPT_4O_MINI,
    temperature: float = 0.0,
    seed: int = 0,
) -> str:
    """Use the OpenAI API to chat with a model.

    Args:
        user_input (str): The user input.
        model_name (OpenAIModels, optional): The model to use. Defaults to OpenAIModels.GPT_4O_MINI.value.
        temperature (float, optional): The temperature. A temperature of 0.0 is deterministic. Defaults to 0.0.
        seed (int, optional): The random seed. Defaults to 0.

    Returns:
        str: The response from the model.
    """

    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    if isinstance(model_name, OpenAIModels):
        model_name = model_name.value

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


def claude(
    user_input: str,
    model_name: Union[ClaudeModels, str] = ClaudeModels.CLAUDE_3_HAIKU,
    temperature: float = 0.0,
    max_tokens: int = 1000,
) -> str:
    """Use the Anthropic API to chat with a Claude model.

    Args:
        user_input (str): The user input.
        model_name (ClaudeModels, optional): The Claude model to use. Defaults to ClaudeModels.CLAUDE_3_HAIKU.value.
        temperature (float, optional): The temperature. A temperature of 0.0 is deterministic. Defaults to 0.0.
        max_tokens (int, optional): The maximum number of tokens to generate. Defaults to 1000.

    Returns:
        str: The response from the Claude model.
    """

    client = Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
    )

    if isinstance(model_name, ClaudeModels):
        model_name = model_name.value

    message = client.messages.create(
        model=model_name,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
    )

    return message.content[0].text
