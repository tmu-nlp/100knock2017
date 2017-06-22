# def test():
#     with open("nlp.txt") as text:
#         for sentence in text:
#             sentence = sentence.strip() #改行を削除。必要かまだ分からん
#             one_line_words = list(sentence) #一行ごとを一文字ごとのリスト化
#             if len(one_line_words) >= 3: #3文字以上じゃないと意味ないし
#                 for count in range(1, len(one_line_words)-1):
#                     if one_line_words[count-1] == ("." or ";" or ":" or "!" or "?") and one_line_words[count] == " " and one_line_words[count+1].isupper():
#                     # .isupper()は全て大文字か、大文字＋大小の区別がない文字の場合にTrueがでる
#                         one_line_words[count] = "\n"
#                 one_line = "".join(one_line_words)
#                 one_line = one_line.split("\n")
#                 for one in one_line:
#                     yield "".join(one)
#
# if __name__ == "__main__":
#     #with open("fifteen_answer.txt", "w") as text:
#         for line in test():
#             print(line)
#             #text.write(line)



# import re
#
# pattern = re.compile(r"[.;:!?] [A-Z]")
#
# with open("nlp.txt") as text:


#suganさんのやつを参考に正規表現で

import re
with open('nlp.txt') as text1, open("fifteen_answer.txt", "w") as text2:
    for line in text1:
        #(. or ; or : or ? or !)
        # replace (group1 group2 group3) by r"group1+group2+\n+group3"
        sentence = re.sub(r"(\;|\!|\:|\.)(\s+)(?P<capital>[A-Z])", r"\1\2\n\2",line)
        text2.write(sentence)

# with open("fifteen_answer.txt", "w") as text, open(""):
    #text.write(sentence)
