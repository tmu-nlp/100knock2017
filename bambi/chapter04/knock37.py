from knock36 import getOrderedFreqList
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
data = getOrderedFreqList()[0:10]
x_label = [x[0] for x in data]
y_pos = [x[1] for x in data]
x_pos = list(range(10))# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
fp = FontProperties(fname='/Library/Fonts/TsukushiAMaruGothic.ttc')
plt.bar(x_pos,y_pos, align='center', alpha=0.5)
plt.xticks(x_pos, x_label, fontproperties=fp)# kind of replace x_pos with x_label
plt.ylabel(r'出現頻度',fontproperties=fp)
plt.title(r'単語の出現頻度',fontproperties=fp)
plt.show()
