from lib1 import f1, f2
import time
import matplotlib.pyplot as plt
import timeit
from tabulate import tabulate

f1_times = []
f2_times = []
N = [1, 5, 10, 15, 20, 25, 30, 35, 40, 41, 42, 43]
x = lambda: f2(a)
for a in N:
    
    
    f1_start = time.perf_counter()
    f1(a)
    f1_end = time.perf_counter()
    f1_times.append(f1_end-f1_start)

    
    

    f2_times.append(timeit.timeit(x))

figure, axis = plt.subplots(1, 2)


col_names = ["n", "fib1", "fib2"]
print(tabulate(list(zip(N,f1_times,f2_times)), headers=col_names, tablefmt="fancy_grid"))

axis[0].plot(N, f1_times)
axis[0].set_title("Fib1")
axis[1].plot(N, f2_times)
axis[1].set_title("Fib2")
plt.show()
