from abc import ABC, abstractmethod
from easytag.common.types import Corpus
from typing import Callable, Iterable
Filter = Callable[[str], str]

class DefaultPreprocessor(ABC):
    """docstring for DefaultPreprocessor."""

    def __init__(self, filters: Iterable[Filter]):
        self._filters = filters

    def preprocess(self, corpus: Corpus) -> Corpus:
        preprocessed_corpus = []
        for doc in corpus:
            s = doc
            for f in self._filters:
                s = f(s)
            preprocessed_corpus.append(s)

        return preprocessed_corpus
