import time
import timeit

import numpy as np

# Time to sum using a generator -- THE BEST CHOICE WITHOUT A Numpy

st = time.time()
lista = (x for x in range(100_000_000))  # 100 millions
soma = sum(lista)
et = time.time()

final = et - st
print()
print('Sum of list using a sum generator:', soma)
print('Execution time of sum is:', round(final, 2), 'seconds')
print()

# Numpy

st_np = time.time()
# lista_np = (x for x in range(100_000_000))
# soma_np = np.sum(np.fromiter(lista_np, int))  # use dtype= or float, but int is more efficient in this case
soma_np = np.sum(np.arange(100_000_000, dtype=int))
et_np = time.time()

final_np = et_np - st_np
print('Sum of list using a sum generator and numpy:', soma_np)
print('Execution time of sum is:', round(final_np, 2), 'seconds')
print()


# timeit, timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000, globals=None) If you run

# time-consuming code with the default number value, it will take a lot of time. So assign less value to the number
# argument Or decide how many samples do you want to measure to get the accurate execution time of a code.
#
# The timeit() functions disable the garbage collector, which results in accurate time capture.
# Also, using the timeit() function, we can repeat the execution of the same code as many times as we want, which
# minimizes the influence of other tasks running on your operating system. Due to this, we can get the more accurate
# average execution time.
def addition():
    print('Sum of list using numpy and timeit:', np.sum(np.arange(100_000_000, dtype=int)))


result = timeit.timeit(addition, number=1)
print(f'Execution time of sum is: {result:.2f} seconds')
print()
