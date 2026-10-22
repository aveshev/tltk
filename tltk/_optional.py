"""Stand-ins for optional dependencies.

g2p, segmentation and romanization need only the standard library. POS
tagging, NER, sentence/EDU segmentation and text analysis need the "nlp"
extra; word vectors and corpus downloads need the "corpus" extra. A missing
library is replaced by a Missing object, which raises an ImportError naming
the extra as soon as it is used.
"""


class Missing:
    def __init__(self, name, extra):
        self._name, self._extra = name, extra

    def _fail(self):
        raise ImportError(f"{self._name} is not installed; it is needed for this tltk feature. "
                          f'Install it with: pip install "tltk[{self._extra}]"')

    def __getattr__(self, attr):
        if attr.startswith("__"):
            raise AttributeError(attr)
        self._fail()

    def __call__(self, *args, **kwargs):
        self._fail()
