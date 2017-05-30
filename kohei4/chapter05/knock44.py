# coding: utf-8
#from collections import defaultdict
import re
import pydot

begin = 0
end =10


class Morph:
    def __init__(self, surface, base, pos, pos1 ):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return 'surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'.\
        format(self.surface, self.base, self.pos, self.pos1)


class Chunk:
    def __init__(self):
        self.morphs = []
        self.dst = -1
        self.srcs = []

    def __str__(self):
        '''print object special function'''
        surface = ''
        for morph in self.morphs:
            surface += morph.surface
        return '{}\tsrcs{}\tdst[{}]'.format(surface, self.srcs, self.dst)

    def sani_surface(self):
        result = ''
        for morph in self.morphs:
            if morph.pos != '記号' :
                result += morph.surface
        return result

    def chk_pos(self, pos):
        for morph in self.morphs:
            if morph.pos == pos:
                return True
        return False

def neco_lines():

    with open('./neko.txt.cabocha','r') as mcb :

        chunks = dict()
        idx = -1


        for line in mcb:
            #line = mcb.readline()
            #print(line)
            if line == 'EOS\n':
                    # Chunkのリストを返す
                if len(chunks) > 0:

                    #for kk, ll in chunks.items():
                    #    print(kk, ll)

                    sorted_tuple = sorted(chunks.items(), key=lambda x: x[0])

                    #for kk, ll in sorted_tuple:
                    #    print(kk, ll)

                    yield (list(zip(*sorted_tuple))[1])

                    #for kk in list(zip(*sorted_tuple))[1]:
                    #    print(kk)

                    chunks.clear()

                else:
                    yield []



            elif line[0] == '*' :
                cabo = line.split(' ')
                idx = int(cabo[1])
                dst = int(re.search(r'(.*?)D', cabo[2]).group(1))
                #print(idx)

                if idx not in chunks:
                    chunks[idx] = Chunk()
                chunks[idx].dst = dst

                if dst != -1:
                    if dst not in chunks:
                        chunks[dst] = Chunk()
                    chunks[dst].srcs.append(idx)


            else:
                #print(st_morph_list)
                line_l = line.replace('\t', ',').split(',')

            #with open('./neko_mecablist.txt','a') as debug:
            #    print(line_l, file = debug)
            # print(line_l)
                chunks[idx].morphs.append(Morph(line_l[0],line_l[7],line_l[1],line_l[2]))
                #print(st_morph_list)
        raise StopIteration

def graph_from_edges_ex(edge_list, title, directed=False):

    if directed:
        graph = pydot.Dot(graph_type='digraph')

    else:
        graph = pydot.Dot(graph_type='graph')



    for edge in edge_list:
        id1 = str(edge[0][0])
        label1 = str(edge[0][1])
        id2 = str(edge[1][0])
        label2 = str(edge[1][1])

        # add node
        graph.add_node(pydot.Node(id1, label=label1))
        graph.add_node(pydot.Node(id2, label=label2))

        # add edege
        graph.add_edge(pydot.Edge(id1, id2))


    graph.set_label( title )

    return graph



for ii, chunks in enumerate(neco_lines()):

    if (ii >= begin) and (ii <= end) :
	# find DST exist
        edges = []
        for i, chunk in enumerate(chunks):
            if chunk.dst != -1:
                # delete punc and confirm existance
                src = chunk.sani_surface()
                dst = chunks[chunk.dst].sani_surface()
                if src != '' and dst != '':
                    edges.append(((i, src), (chunk.dst, dst)))
        if len(edges) > 0:
            title = "我輩は猫である。  " + str(ii + 1) + "行"
            graph = graph_from_edges_ex(edges, title, directed=True)
            graph.write_png('result.png')
