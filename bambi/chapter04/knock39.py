from knock36 import getOrderedFreqList
import matplotlib.pyplot as plt
data = getOrderedFreqList()
freq = [x[1] for x in data]
plt.xscale("log")
plt.yscale("log")
plt.plot(freq)
plt.show()
