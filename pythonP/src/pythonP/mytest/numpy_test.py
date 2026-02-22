import numpy as np
from numpy._typing import NDArray

def basic_math()->None:
    a:NDArray[np.int_] = np.array([10,20,30,40])
    b:NDArray[np.int_] = np.array([1,2,3,4])

    addition:NDArray[np.int_] = np.add(a,b)
    print(f"add result: {addition}")

    subtraction:NDArray[np.int_] = np.subtract(a, b)
    print(f"subtraction result: {subtraction}")

    multiplication:NDArray[np.int_] = np.multiply(a,b)
    print(f"multiplication result: {multiplication}")

    division:NDArray[np.int_] = np.divide(a,b)
    print(f"division result: {division}")

    exponential:NDArray[np.int_] = np.exp(b)
    print(f"exponential result: {exponential}")

    logaritm:NDArray[np.int_] = np.log(a)
    print(f"log result: {logaritm}")

def array_concat_split()->None:
    arr1:NDArray[np.int_] = np.array([1,2,3,4])
    concat_arr:NDArray[np.int_] = np.concatenate((arr1, np.array([5, 6,7])))
    print(f"concat array: {concat_arr}")

    split_arr:list[NDArray[np.int_]] = np.split(concat_arr, [3])
    print(f"split array: {split_arr}")

def reshape_test()->None:
    arr3:NDArray[np.int_] = np.array([1,2,3,4,6,8])
    new_arr:NDArray[np.int_] = arr3.reshape(3,2)
    print(f"reshape arr3: \n{new_arr}")

def basic_ex()->None:
    arr1:NDArray[np.int_] = np.array([1,2,3,4])
    print("one dimensional: ", arr1)

    arr2:NDArray[np.int_] = np.array([[1,2,3],[4,5,6]])
    print("two dimensional: \n", arr2)

    print("shape: ", arr2.shape)
    print("arr2 size: ", arr2.size)
    print("arr2 dimensional: ", arr2.ndim)
    print("arr2 data type: ",arr2.dtype)

    print(f"arr1 -> 1st: {arr1[0]}")
    print(f"arr1 -> 2 - 4: {arr1[2:4]}")

    print(f"arr2 -> 1 row 2 column: {arr2[0,1]}")
    print(f"arr2 -> 2 row: {arr2[1,:]}")

def numpy_example()->None:
    print(f"numpy example")
    # basic_ex()
    # reshape_test()
    # array_concat_split()
    basic_math()

