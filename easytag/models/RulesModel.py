from easytag.common import types
from collections import namedtuple
from typing import Iterable, List
from easytag.common.types import Doc, LabelRules, Rule, Label, LabelTag, CorpusTags


class RulesModel(object):
    """docstring for RulesModel."""

    def __init__(self, labels_rules: Iterable[LabelRules]):
        self._labels_rules: Iterable[LabelRules] = labels_rules

    def apply_rules(self, doc: Doc) -> List[LabelTag]:
        """
        Apply rules to doc.

        Each rule is tested against the doc.

        Args:
            doc (Doc): Document

        Returns:
            List[bool]: resulting boolean value for each rule

        Raises:
            Exception: description

        """
        res = [lr.apply_rule(doc) for lr in self._labels_rules]
        return res


    def tag(self, corpus: Iterable[Doc]) -> CorpusTags:
        """
        Tag whole corpus.

        For every doc in corpus apply all rules and return boolean values.

        Args:
            corpus (Iterabe[Doc]): a corpus of docs

        Returns:
            CorpusTags: tagged corpus

        Raises:
            Exception: description

        """

        docs_tagged = []
        for doc in corpus:
            docs_tagged.append(self.apply_rules(doc))
        return docs_tagged
