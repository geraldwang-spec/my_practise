from itertools import zip_longest
import numpy as np
from numpy.typing import NDArray

class array_practice:
    def OneArray_01(self)->None:
        a: NDArray[np.long] = np.random.randint(0, 10, 10)
        print(f"one array = {a}")
        b:NDArray[np.long] = np.sort(a)[::-1]
        print(f"sort(a) = {np.sort(a)}, rever = {b}")

    def OneArray_03(self)->None:
        rand: NDArray[np.int_] = np.random.randint(0, 100, 30, dtype=np.int_)
        print(f"orignal = {rand}")
        even: NDArray[np.int_] = np.sort( rand[rand % 2 == 0])[::-1]
        odd: NDArray[np.int_] = np.sort(rand[rand % 2 != 0])[::-1]
        print(f"odd = {odd}")
        print(f"even = {even}")

        for o, e in zip_longest(odd, even, fillvalue=0):
            print(f"odd/even = {o}, {e}")

        max_len: int = max(len(odd), len(even))
        odd_padded:NDArray[np.int_] = np.pad(odd, (0, max_len - len(odd)), mode='constant',  constant_values=0)
        even_padded:NDArray[np.int_] = np.pad(even, (0, max_len - len(even)), mode='constant',  constant_values=0)

        for i in range(max_len):
            print(f"odd/even= {odd_padded[i]}, {even_padded[i]}")


def numpy_real_example()->None:
    print("umpy real example")
    arrayP:array_practice = array_practice()
    # arrayP.OneArray_01()
    arrayP.OneArray_03()
