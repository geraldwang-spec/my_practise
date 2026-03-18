import sys
from pythonP.advance_example.Character_Input_adv import advance_character_input
from pythonP.advance_example.leetcode import leetCode_test
from pythonP.conditions import conditionsOperators
from pythonP.dictionaries import dictionaries_example
from pythonP.io import io_example
from pythonP.list import list_practise
from pythonP.mytest import fastapi_test
from pythonP.mytest.class_practise import class_practise_test
from pythonP.mytest.lambdatest import lambda_example
from pythonP.mytest.numpy_real_test import numpy_real_example
from pythonP.mytest.numpy_test import numpy_example
from pythonP.mytest.scipy_test import scipy_example
from pythonP.practice_example import practice_ex
from pythonP.mytest.exceptions_example import exception_example
from stocks_project.stocks_main import stock_init

def add(a, b):
    return a + b

def practise():
    # conditionsOperators()
    # list_and_tuples()
    # list_practise()
    # dictionaries_example()
    # io_example()
    # practice_ex()
    # advance_character_input()
    # lambda_example()
    # exception_example()
    # numpy_example()
    # leetCode_test()
    # numpy_real_example()
    # scipy_example()
    class_practise_test()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        practise()
    else:
        if sys.argv[1] == "stocks":
            stock_init()
    # print(f'Sum: {add(1, 2)}')
