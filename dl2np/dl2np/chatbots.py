import os
from enum import Enum
from openai import OpenAI
from anthropic import Anthropic
from dl2np.utils import get_logger

logger = get_logger(__name__)


class ChatModel:
    class OpenAIModels(Enum):
        GPT_4O_MINI = "gpt-4o-mini"
        GPT_4O = "gpt-4o"
        GPT_4_TURBO = "gpt-4-turbo"
        GPT_4 = "gpt-4"
        GPT_35_TURBO = "gpt-35-turbo"

    class AnthropicModels(Enum):
        CLAUDE_3_OPUS = "claude-3-opus-20240229"
        CLAUDE_3_SONNET = "claude-3-sonnet-20240229"
        CLAUDE_3_HAIKU = "claude-3-haiku-20240307"
        CLAUDE_35_SONNET = "claude-3-5-sonnet-20240620"

    def __init__(self, model_name: str):
        self.model_name = model_name
        self.set_model_type()
        self.set_client()

    def is_openai(self) -> bool:
        return self.model_type in self.OpenAIModels

    def is_anthropic(self) -> bool:
        return self.model_type in self.AnthropicModels

    def set_model_type(self):
        # Match an OpenAIModels Enum to the model_name
        if self.model_name.startswith("gpt"):
            self.model_type = self.OpenAIModels(self.model_name)
        # Match an AnthropicModels Enum to the model_name
        elif self.model_name.startswith("claude"):
            self.model_type = self.AnthropicModels(self.model_name)
        else:
            raise ValueError("Invalid model_name. Must start with 'gpt' or 'claude'.")

    def set_client(self):
        if self.is_openai():
            api_key = os.getenv("OPENAI_API_KEY")
            self.client = OpenAI(api_key=api_key)
        elif self.is_anthropic():
            api_key = os.getenv("ANTHROPIC_API_KEY")
            self.client = Anthropic(api_key=api_key)
        else:
            raise ValueError("Invalid model_name.")

    def chat(
        self,
        user_input: str,
        temperature: float = 0.0,
        seed: int = 0,
        max_tokens: int = 4096,
    ) -> str:
        if self.is_openai():
            logger.info("Using OpenAI model.")
            return self._openai_chat(user_input, temperature, seed)
        elif self.is_anthropic():
            logger.info("Using Anthropic model.")
            return self._anthropic_chat(user_input, temperature, max_tokens)
        else:
            raise ValueError("Invalid model_name.")

    def _openai_chat(
        self,
        user_input: str,
        temperature: float = 0.0,
        seed: int = 0,
    ) -> str:
        return self._send_receive(
            user_input=user_input,
            temperature=temperature,
            seed=seed,
        )

    def _anthropic_chat(
        self,
        user_input: str,
        temperature: float = 0.0,
        max_tokens: int = 4096,
    ) -> str:
        return self._send_receive(
            user_input=user_input,
            temperature=temperature,
            max_tokens=max_tokens,
        )

    def _send_receive(
        self,
        user_input: str,
        temperature: float,
        max_tokens: int = 4096,
        seed: int = 0,
    ) -> str:
        logger.debug(f"Sending user input to {self.model_name}: {user_input}")

        logger.info(f"Sending to {self.model_name}...")
        logger.debug(f"User input: {user_input}")

        if self.is_openai():
            if not isinstance(self.client, OpenAI):
                raise ValueError("Invalid client.")
            message = self.client.chat.completions.create(
                messages=[{"role": "user", "content": user_input}],
                model=self.model_name,
                temperature=temperature,
                seed=seed,
            )
            out = message.choices[0].message.content
        elif self.is_anthropic():
            if not isinstance(self.client, Anthropic):
                raise ValueError("Invalid client.")
            message = self.client.messages.create(
                model=self.model_name,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[{"role": "user", "content": user_input}],
            )
            out = message.content[0].text

        logger.info(f"Received from {self.model_name}...")
        if out is None:
            raise ValueError("No response from the model.")
        return out


def chat(user_input: str, model_name: str) -> str:
    chat_model = ChatModel(model_name)
    return chat_model.chat(user_input)
