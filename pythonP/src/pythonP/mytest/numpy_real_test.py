from itertools import zip_longest
import numpy as np
from numpy.typing import NDArray
# from typing import cast

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

    def OneArray_04(self)->None:
        box: NDArray[np.int_] = np.random.randint(0, 20, 30, dtype=np.int_)
        temp_result: list[int] = []
        print(f"box = {box}")

        for i in range(len(box)):
            if box[i] == 8:
                temp_result.append(i)

        result: NDArray[np.int_] = np.array(temp_result, dtype=np.int_)

        if len(result) == 0:
            print(f"this box has not 8")
        else:
            print(f"result = {result}")

    def OneArray_04_adv(self)->None:
        box: NDArray[np.int_] = np.random.randint(0, 20, 30, dtype=np.int_)
        print(f"box = {box}")

        # result: NDArray[np.int_] = np.where(cast(NDArray[np.bool_], box == 8))[0] # must from typing import cast
        result: NDArray[np.int_] = np.where(np.equal(box, 8))[0]
        if result.size == 0:
            print(f"this box has not 8")
        else:
            print(f"result = {result}")

    def OneArray_05(self)->None:
        array: list[int] = np.random.randint(0, 30, 10, dtype=np.int_).tolist()
        # array: list[int] = [10,8,9,3,4,5,6,7,1, 1]
        print(f"array = {array}")
        min_vol:int = min(array)
        print(f"min = {min_vol}")
        # result: list[int] = np.where(np.equal(array, min_vol))[0].tolist()
        result: list[int] = [i for i, x in enumerate(array) if x == min_vol]
        print(f"result = {result}")
        for item in range(len(result)):
            if result[item] == len(array) - 1 - item:
                continue

            array[result[item]] ^= array[-1 * item - 1]
            array[-1 * item - 1] ^= array[result[item]]
            array[result[item]] ^= array[-1 * item - 1]

        print(f"result = {array}")



def numpy_real_example()->None:
    print("umpy real example")
    arrayP:array_practice = array_practice()
    # arrayP.OneArray_01()
    # arrayP.OneArray_03()
    # arrayP.OneArray_04()
    # arrayP.OneArray_04_adv()
    arrayP.OneArray_05()
