from easytag.models import Model
from typing import Iterable
Doc = Iterable[str]

class Tagger(object):
    """docstring for Tagger."""

    def __init__(self, reader: Reader = None, preprocessor: Preprocessor = None,
                 model: Model = None, postprocessor: Postprocessor = None):
        super(Tagger, self).__init__()
        self._reader = reader
        self._preprocessor = preprocessor
        self._model = model
        self._postprocessor = postprocessor

    def tag(self, doc: Doc):
        return self._model.tag(doc)


    def run(self):
        """
        Run tagger on corpus.

        Apply preprocessors (if any), models (if any) and postprocessors (if any)
        to given corpus.

        Returns:
            type: description

        Raises:
            Exception: description

        """
        corpus = self.reader.read()

        if self._preprocessor:
            corpus = self._preprocessor.preprocess(corpus)

        tags = [self._model.tag(item) for item in corpus]
