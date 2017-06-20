import xml.etree.ElementTree as et
import re

if __name__ == '__main__':
        with open('nlp.txt.xml') as i_f:
            par = et.parse(i_f)
            for sentence in par.iter('sentence'):
                txt = sentence.find('parse').text
                layer = 0
                NPlayer = [0]
                for i in range(len(txt)):
#                    print(txt[i], end = '')
                    if txt[i] == '(':
                        layer += 1
                    elif txt[i] == ')':
                        layer -= 1


                    if txt[i:i+3] == '(NP':
                        NPlayer.append(layer - 1)
                        s_point = i+4

                    if NPlayer[-1] > 0 and layer > NPlayer[-1]:
                        continue
                    elif NPlayer[-1] != 0:
#                        print(txt[s_point:i])
                        output = re.sub('\([A-Z]*', '', txt[s_point:i])
                        output = re.sub('\)*', '', output)
                        print(output)
                        del NPlayer[-1]
