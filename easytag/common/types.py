from typing import List, Iterable, Callable, NamedTuple

from dataclasses import dataclass

Doc = Iterable[str]
Label = str
Corpus = Iterable[str]

@dataclass
class LabelTag:
    label: Label
    tag: bool

CorpusTags = List[List[LabelTag]]
