from typing import Any, List, Optional
from langchain.llms.base import LLM
from langchain.callbacks.manager import CallbackManagerForLLMRun
import ollama

class OllamaLLM(LLM):
    model: str = "llama3.2:3b"
    temperature: float = 0.7

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        response = ollama.generate(
            model=self.model,
            prompt=prompt,
            options={
                "temperature": self.temperature,
            }
        )
        return response['response']

    @property
    def _llm_type(self) -> str:
        return "ollama"
