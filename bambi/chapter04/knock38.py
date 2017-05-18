from knock36 import getOrderedFreqList
import matplotlib.pyplot as plt
data = getOrderedFreqList()[0:30]
freq = [x[1] for x in data]
plt.hist(freq,range=(1,10000),histtype="barstacked")
plt.grid()
plt.show()
