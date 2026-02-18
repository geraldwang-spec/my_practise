import numpy as np
from numpy._typing import NDArray

def basic_ex()->None:
    arr1:NDArray[np.int_] = np.array([1,2,3,4])
    print("one dimensional: ", arr1)

    arr2:NDArray[np.int_] = np.array([[1,2,3],[4,5,6]])
    print("two dimensional: \n", arr2)


def numpy_example()->None:
    print(f"numpy example")
    basic_ex()
