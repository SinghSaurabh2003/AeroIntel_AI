from abc import ABC, abstractmethod


class BaseLLM(ABC):

    @abstractmethod
    def get_llm(self):
        """Return a LangChain chat model."""
        pass