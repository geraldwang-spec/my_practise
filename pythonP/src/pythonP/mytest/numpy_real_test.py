import numpy as np
from numpy.typing import NDArray

class array_practice:
    def OneArray_01(self)->None:
        a: NDArray[np.long] = np.random.randint(0, 10, 10)
        print(f"one array = {a}")
        b:NDArray[np.long] = np.sort(a)[::-1]
        print(f"sort(a) = {np.sort(a)}, rever = {b}")

        



def numpy_real_example()->None:
    print("umpy real example")
    arrayP:array_practice = array_practice()
    arrayP.OneArray_01()
