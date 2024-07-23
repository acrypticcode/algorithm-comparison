from lib1 import f2
import time
import matplotlib.pyplot as plt
from tabulate import tabulate

f2_times = []
N = [0,10,12,14,16,18,19,20]
for a in N:
    print(a)
    f2_start = time.perf_counter()
    f2(2**a)
    f2_end = time.perf_counter()
    f2_times.append(f2_end-f2_start)
    
plt.plot(N, f2_times)
plt.show()
