from typing import Callable, ParamSpec, TypeVar

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
    decorators_example()




