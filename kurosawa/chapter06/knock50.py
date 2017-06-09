import sys

def separate_sentence():
    with open(sys.argv[1]) as text:
        for line_sep in text:
            line_sep = line_sep.strip()
            line_sep = list(line_sep)
            if len(line_sep) >= 3:
                for i in range(1,len(line_sep)-1):
                    if line_sep[i-1]==('.' or ';' or '?' or '!') and line_sep[i]==' ' and line_sep[i+1].isupper():
                        line_sep[i] = '\n'
                line_sep = ''.join(line_sep)
                line_sep = line_sep.split('\n')
                for line_sen in line_sep:
                    yield ''.join(line_sen)

if __name__ == '__main__':
    for line in separate_sentence():
        print(line)

