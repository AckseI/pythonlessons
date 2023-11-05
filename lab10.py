"""
Написать функцию, которая создает массив из всех четных элементов между 50 и 90.
"""

import numpy as np

arr = []
for i in range(50, 90+1):
    if i % 2 == 0:
        arr.append(i)

array = np.array(arr)
print(array)
