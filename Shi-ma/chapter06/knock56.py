import xml.etree.ElementTree as ET
import collections

def set_replace_dict(replace_dict):
    for key_dict, value_dict in replace_dict.items():
        if len(value_dict) >= 2:
            temp_value_dict = value_dict[:]
            for i, temp_i in enumerate(temp_value_dict[:-1]):
                temp_i_list = temp_i.split('_*_')
                for j, temp_j in enumerate(temp_value_dict[i+1:]):
                    temp_j_list = temp_j.split('_*_')
                    if temp_i_list[0] == temp_j_list[0]:
                        if int(temp_i_list[1]) >= int(temp_j_list[1]):
                            value_dict.remove(temp_j)
                        else:
                            value_dict.remove(temp_i)
                    elif temp_i_list[1] == temp_j_list[1]:
                        if int(temp_i_list[0]) <= int(temp_j_list[0]):
                            value_dict.remove(temp_i)
                        else:
                            value_dict.remove(temp_j)
            value_dict.sort(key=lambda x: int(x.split('_*_')[0]))

def make_replace_dict(data_in_path):
    tree = ET.parse(data_in_path)
    root = tree.getroot()
    replace_dict = collections.defaultdict(lambda: [])
    for i, coreference in enumerate(root.findall(".//coreference")):
        for mention in coreference.findall('mention'):
            if mention.get('representative'):
                rep_mention = mention.find('text').text
            else:
                key = int(mention.find('sentence').text)
                value = mention.find('start').text + '_*_' + mention.find('end').text + '_*_' + mention.find('text').text + '_*_' + rep_mention
                replace_dict[key].append(value)
    set_replace_dict(replace_dict)
    return replace_dict

def make_replace_text(data_in_path, data_out):
    tree = ET.parse(data_in_path)
    root = tree.getroot()
    replace_dict = make_replace_dict(data_in_path)
    for sentence in root.findall(".//sentences/sentence"):
        if len(replace_dict[int(sentence.get('id'))]) == 0:
            for token in sentence.iter('token'):
                print(token.find('word').text, end=' ', file=data_out)
        else:
            flag_replace = 0
            count_value = 0
            replace = replace_dict[int(sentence.get('id'))][count_value].split('_*_')
            for token in sentence.iter('token'):
                if token.get('id') == replace[0]:
                    print('「{} ({})」'.format(replace[3], replace[2]), end=' ', file=data_out)
                    flag_replace = 1
                elif token.get('id') == replace[1]:
                    print(token.find('word').text, end=' ', file=data_out)
                    count_value += 1
                    if count_value < len(replace_dict[int(sentence.get('id'))]):
                        replace = replace_dict[int(sentence.get('id'))][count_value].split('_*_')
                    flag_replace = 0
                elif flag_replace == 0:
                    print(token.find('word').text, end=' ', file=data_out)
        print('', file=data_out)

if __name__ == '__main__':
    with open('knock56_result.txt', 'w') as data_out:
        data_in_path = '../data/knock50_result.txt.xml'
        make_replace_text(data_in_path, data_out)
