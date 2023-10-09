import random
from matplotlib import pyplot as plt
import math
import numpy as np

sigma = 2
m = 0.5

n = 200
N = int(math.log2(n))

x = np.array([])
for i in range(n):
    sum_elements = 0
    for j in range(12):
        sum_elements += random.random()
    x = np.append(x, sum_elements - 6)
    

y = np.array([])
for element in x:
    y = np.append(y, sigma * element + m)

min_value = int(min(y))
max_value = int(max(y)) + 1

step = (max_value - min_value) / N
intervals = np.arange(float(min_value), float(max_value), step)
intervals = np.append(intervals, max_value)

intervals_values = np.zeros(len(intervals), dtype=int)
for value in y:
    for index in range(len(intervals)):
        if value <= intervals[index]:
            intervals_values[index] += 1
            break

print(intervals)
print(intervals_values)
intervals_values = np.array([value / n for value in intervals_values])

plt.title('Гистрограмма распределения')
plt.plot(intervals, intervals_values)
plt.show()
