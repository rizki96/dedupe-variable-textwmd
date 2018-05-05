from __future__ import print_function

from dedupe.variables.base import DerivedType, FieldType
from dedupe import predicates

from gensim.models import KeyedVectors

class TextWMDistance(object):
    def __init__(self, word2vec_format, other_fields=None):
        self.model = KeyedVectors.load_word2vec_format(word2vec_format)
        self.model.init_sims(replace=True)

    def __call__(self, field_1, field_2):
        if field_1 == field_2:
            return 1.0

        else:
            distance = self.model.wmdistance(field_1, field_2)
            return 1.0 - distance


class TextWMDType(FieldType):
    type = "TextWmd"
    _predicate_functions = [predicates.wholeFieldPredicate]
    
    def __init__(self, definition):
        super(TextWMDType, self).__init__(definition)
        
        self.comparator = TextWMDistance(definition['word2vec_format'],
                                definition['other_fields'])
