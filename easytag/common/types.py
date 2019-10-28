from typing import List, Iterable, Callable, NamedTuple

from dataclasses import dataclass

Doc = Iterable[str]
Rule = Callable[[Doc], bool]
Label = str
Corpus = Iterable[Doc]

@dataclass
class LabelTag:
    label: Label
    tag: bool

@dataclass
class LabelRules:
    label: Label
    rules: List[Rule]
    def apply_rule(self, doc:Doc):
        return any([rule(doc) for rule in self.rules])

CorpusTags = List[List[LabelTag]]
