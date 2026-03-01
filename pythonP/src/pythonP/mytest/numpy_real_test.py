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
        # result: list[int] = np.where(np.equal(array, min_vol))[1].tolist()
        result: list[int] = [i for i, x in enumerate(array) if x == min_vol]
        print(f"result = {result}")
        for item in range(len(result)):
            left_idx: int = result[item]
            right_idx_pos:int = len(array) - 1 - item
            right_idx_neg:int = -1 * item - 1
            if left_idx == right_idx_pos:
                print(f"Skip index {left_idx}: same position, XOR would result in 0")
                continue

            array[left_idx] ^= array[right_idx_neg]
            array[right_idx_neg] ^= array[left_idx]
            array[left_idx] ^= array[right_idx_neg]

        print(f"result = {array}")

    def OneArray_05_adv(self)->None:
        # array: list[int] = np.random.randint(0, 30, 10, dtype=np.int_).tolist()
        array: list[int] = [10,10,2]
        print(f"array = {array}")
        min_vol:int = min(array)
        print(f"min = {min_vol}")
        # result: list[int] = np.where(np.equal(array, min_vol))[1].tolist()
        indices: list[int] = [i for i, x in enumerate(array) if x == min_vol]
        print(f"indices = {indices}")

        for i, left_idx in enumerate(indices):
            right_idx: int = len(array) - 1 - i

            if left_idx == right_idx:
                print(f"Skip index {left_idx}: same position, XOR would result in 0")
                continue

            # 使用 Pythonic Swap，安全且防呆
            array[left_idx], array[right_idx] = array[right_idx], array[left_idx]
        print(f"Final:    {array}")# 使用 Pythonic Swap，安全且防呆

    def OneArray_06(self)->None:
        person:list[int] = np.ones(17, dtype=int).tolist()
        print(f"person = {person}")

        index: int = 0 
        number: int = 0
        while person.count(1) > 1:
            current_index: int = index % 17
            
            if person[current_index] == 1:
                number += 1
                if number % 3 == 0:
                    person[current_index] = 0
            
            index += 1

        print(f"person = {person}")
        indices:list[int] = [ i for i, x in enumerate(person) if x == 1]
        print(f"last position = {indices}")

    def OneArray_06_adv(self)->None:
        person:list[int] = list(range(17))
        print(f"person = {person}")

        index: int = 0
        step: int = 3
        while len(person) > 1:
            index = (index + step - 1) % len(person)
            removed = person.pop(index)
        print(f"last person = {person[0]}")

def numpy_real_example()->None:
    print("umpy real example")
    arrayP:array_practice = array_practice()
    # arrayP.OneArray_01()
    # arrayP.OneArray_03()
    # arrayP.OneArray_04()
    # arrayP.OneArray_04_adv()
    # arrayP.OneArray_05()
    # arrayP.OneArray_05_adv()
    # arrayP.OneArray_06()
    arrayP.OneArray_06_adv()
