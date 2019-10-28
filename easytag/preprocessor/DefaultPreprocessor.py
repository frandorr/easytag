from abc import ABC, abstractmethod
from easytag.common.types import Corpus

class DefaultPreprocessor(ABC):
    """docstring for DefaultPreprocessor."""

    def __init__(self, corpus: Corpus):
        self._corpus = corpus
    def preprocess(self) -> Corpus:
        return self._corpus
