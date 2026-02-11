from typing import Callable


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




