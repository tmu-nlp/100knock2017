class Morph:
    def __init__(self, sentence_id, chunk_id, tok_id, tok_feature, tok_surface):
        self._sentence_id = sentence_id
        self._chunk_id = chunk_id
        self._tok_id = tok_id
        self._tok_list = tok_feature.split(',')
        self._feature_dict = \
        {'surface':tok_surface, 'base':self._tok_list[6], \
        'pos':self._tok_list[0], 'pos1':self._tok_list[1]}
        self._tok_body = tok_surface
        self._tok_pos = self._tok_list[0]
        self._tok_pos1 = self._tok_list[1]

    @property
    def feature(self):
        return self._tok_list

    @property
    def token_id(self):
        return self._tok_id

    @property
    def token_body(self):
        return self._tok_body

    @property
    def token_body_exclude_symbol(self):
        # print(self._tok_pos)
        if self._tok_pos != '記号':
            return self._tok_body
        else:
            return "sym"#for debug

    @property
    def sentence_id(self):
        return self._sentence_id

    @property
    def solve_knock40(self):
        return self._feature_dict

    @property
    def chunk_id(self):
        return self._chunk_id

    @property
    def token_pos(self):
        return self._tok_pos

    @property
    def features(self):
        return self._feature_dict

    @property
    def token_pos1(self):
        return self._tok_pos1

