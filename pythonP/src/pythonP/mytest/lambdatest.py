import doctest
from typing import Any, Callable, ParamSpec, TypeVar
import unittest
# from typing import Any, Callable

def doctest_example()->None:
    print("doctest example")
    addtwo:Callable[[int, int], int] = lambda x, y: x + y
    addtwo.__doc__ = """
    >>> addtwo(1,2)
    3
    >>> addtwo(-1,5)
    4
    """
    # _ = doctest.testmod(verbose=True)
    # 這裡還有一個關鍵：因為 addtwo 是在函數內定義的局部變數，
    # doctest.testmod() 預設掃描的是全域（Module）層級。
    # 我們需要手動把 addtwo 塞進 globs 參數裡。
    _ = doctest.run_docstring_examples(addtwo, globs={'addtwo': addtwo}, verbose=True)


def add(a:int , b:int )->int:
    return a + b

class TestMathFunction(unittest.TestCase):
    # 測試案例必須以 test_ 開頭
    def test_add_positive(self)->None:
        self.assertEqual(add(1, 2), 3)

    def test_add_negative(self)->None:
        self.assertEqual(add(-1, -1), -2)

def unittest_example()->None:
    print("unittest example")
    _= unittest.main(module='__main__', argv=[''], exit = False)

def make_counter(start_at: int = 0)->Callable[[],int]:
    count = start_at
    def counter()->int:
        nonlocal count
        count += 1 
        return count
    
    return counter

def counter_example()->None:
    c1 = make_counter(10)
    c2 = make_counter(100)
    print(f"c1 = {c1()}")
    print(f"c1 = {c1()}")
    print(f"c2 = {c2()}")

def evaluation_time()->None:
    numbers = 'one', 'two', 'three'
    fnucs:list[Callable[[], Any]]  = []

    for n in numbers:
        fnucs.append(lambda: print(n))

    n = 'apple'
    for f in fnucs:
        f()

def outer_func1(x: int)->Callable[[int], int]:
    y = 4
    return lambda z: x+y+z


def outer_func(x:int)->Callable[[int], int]:
    y = 4
    def inner_func(z: int)->int:
        print(f"x={x}, y={y}, z={z}")
        return x + y +z
    return inner_func

def closure_example()->None:
    print(f"closure_example")
    for i in range(3):
        closure: Callable[[int], int] = outer_func(i)
        print(f"clourse({i+5}) = {closure(i+5)}")

    for i in range(3):
        closure1: Callable[[int], int] = outer_func1(i)
        print(f"closure1({i+5}) = {closure1(i+5)}")


P = ParamSpec("P")
R = TypeVar("R")

def some_decorator(f: Callable[P, R])->Callable[P,R]:
    def wraps(*args: P.args, **kwargs: P.kwargs) -> R:
        """this is decorator of wraps"""
        print(f"--- 裝飾器啟動：準備呼叫 {f.__name__} ---")
        return f(*args, **kwargs)
    return wraps

@some_decorator
def decorators_function(x: str) -> None:
    """ths is test decorator function"""
    print(f"execution this function: print {x}")

@some_decorator
def decorators_function1(x:int)->None:
    """this is decorated function1 test int """
    print(f"print x = {x}")

def decorators_example()->None:
    print("1. 呼叫函數的結果：")
    decorators_function("Hello")

    print("\n2. 檢查函數的名字 (__name__)：")
    # 如果沒有被掉包，應該印出 "decorated_function"
    # 但因為被裝飾了，它現在會印出裝飾器內部的 "wraps"
    print(f"目前的函數名稱是: {decorators_function.__name__}")

    print("\n3. 檢查函數的說明文件 (__doc__)：")
    # 原本的註解也會消失，因為現在的名字指向 wraps
    print(f"目前的說明文件是: {decorators_function.__doc__}")

    decorators_function1(10)

    print("\n2. 檢查函數的名字 (__name__)：")
    # 如果沒有被掉包，應該印出 "decorated_function"
    # 但因為被裝飾了，它現在會印出裝飾器內部的 "wraps"
    print(f"目前的函數名稱是: {decorators_function1.__name__}")

    print("\n3. 檢查函數的說明文件 (__doc__)：")
    # 原本的註解也會消失，因為現在的名字指向 wraps
    print(f"目前的說明文件是: {decorators_function1.__doc__}")

def basic_test()->None:
    func:Callable[[int], int] = lambda x: x+1
    _c:int = func(2)
    print(f"_c = {_c}")

    func1:Callable[[], None] = lambda : print("QOO")
    func1()

    func2:Callable[[int,int],int] = lambda x,y: x+y
    print(f"result = {func2(2,3)}")

    func3: Callable[[int, Callable[[int],int]], int] = lambda x, func: x + func(x)
    print(f"func3 = {func3(5, lambda x:  x * 2)}")

    func4: Callable[[int],float] = lambda x: x/1
    print(f"func4 = {func4(2)}")


def lambda_example()-> None:
    print("lambda_example")
    # basic_test()
    # decorators_example()
    # closure_example()
    # evaluation_time()
    # counter_example()
    # unittest_example()
    doctest_example()




