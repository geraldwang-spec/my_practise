import os
import time

def boolOperators():
    name = "John"
    age  = 23
    if name == "John" and age == 23:
        print(f"Your name is {name}, and your are {age} years old")

    if name == "John" or name == "Rick":
        print("Your name is either John or Rick")

def inOperator():
    name = "John"
    if name in ["Rick", "Johdd"]:
        print("Your name is either John or Rick.")

def ifelseOperator():
    statement = False
    another_statement = False
    if statement is True:
        print("statement is true")
    elif another_statement is True:
        print("another_statement is true")
    else:
        print("if else finial item")

def isOperatorArray():
    x = [1,2,3]
    y = [1,2,3]
    z = y
    print(x == y)
    print(x is y)
    print(f"x id:{id(x)}")
    print(f"y id:{id(y)}")
    print(f"y hex id:{hex(id(y))}")
    # time.sleep(1000)
    print(f"z id:{id(z)}")

def notOperator():
    print(not False)
    print(not True)
    if not 2 == 2 :
        print("dd")

def conditionsOperators():
    # boolOperators()
    # inOperator()
    # ifelseOperator()
    # isOperatorArray()
    notOperator()

