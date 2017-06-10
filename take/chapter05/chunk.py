from morph import Morph

class Chunk:
    def __init__(self, sentence_id, c_id, c_link, c_rel, c_score, c_head, c_func, mor_list):
        self._c_id = c_id
        self._c_link = c_link
        self._c_rel = c_rel
        self._c_score = c_score
        self._c_head = c_head
        self._c_func = c_func
        self._sentence_id = sentence_id
        self._morphs = mor_list
        self.index = 0
        self.substituted = False

    @property
    def cid(self):
        return int(self._c_id)

    @property
    def link(self):
        return int(self._c_link)

    @property
    def rel(self):
        return self._c_rel

    @property
    def score(self):
        return float(self._c_score)

    @property
    def head(self):
        return int(self._c_head)

    @property
    def func(self):
        return int(self._c_func)

    @property
    def sentence_id(self):
        return int(self._sentence_id)

    @property
    def morphs(self):
        return self._morphs

    @property
    def allbody(self):
        ret = ''
        for x in self.morphs:
            ret += x.token_body
        return ret

    @property
    def allbody_exclude_symbol(self):
        ret = ''
        for x in self.morphs:
            ret += x.token_body_exclude_symbol
        return ret

    @property
    def has_noun(self):
        # poslst = [x.token_pos for x in self._morphs]
        # print('has 名詞-> {}: {}'.format('名詞' in poslst, poslst))
        return '名詞' in [x.token_pos for x in self._morphs]

    @property
    def has_verb(self):
        # poslst = [x.token_pos for x in self._morphs]
        # print('has 動詞-> {}: {}'.format('動詞' in poslst, poslst))
        return '動詞' in [x.token_pos for x in self._morphs]

    @property
    def first_verb(self):
        for mor in self.morphs:
            if mor.token_pos == '動詞':
                return mor.features['base'], self.cid, self.sentence_id
                    # return int(mor._tok_id)
            return None,-100,-100

    def substitute_to(self, x):
        for m in self.morphs:
            if m.token_pos == '名詞':
                m.subX(x)
                # m._tok_body = 'X'
                break
        self.substituted = True

    def revert_subX(self):
        for m in self.morphs:
            if m.token_pos == '名詞':
                m.revert_subX()
                break

    @property
    def allbody_exc_symbol_as_list(self):
        return ''.join([m.token_body for m in self.morphs if not m.token_pos == '記号'])
    
    def is_root(self):
        return self.link == -1