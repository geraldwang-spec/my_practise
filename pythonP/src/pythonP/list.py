from typing import Any
import json

def list_and_tuples():
    color: list[Any] = ["red", "green", "blue", "yellow"]
    person = ("Jane", 25, "python developer", "Canada")

    for i in range(4):
        print(f"color = {color[i]}\tperson = {person[i]}")
        if i == 2:
            color[i] = 33
            # person[i] = "iii" #tuple object does not support item assignment
            print(f"i=2 color = {color[i]}\tperson = {person[i]}")

def list_and_range():
    digits = list(range(10))
    print(f"digits = {digits}")

    even_digits = [n for n in range(1, 10) if n%2 == 0]
    print(f"even_digits={even_digits}")

    double_even = [n**2 for n in range(1, 10) if n%2 == 0]
    print(f"double_even = {double_even}")

def advance_operator():
    num = [n for n in range(1,10) if n**2%2 == 0]
    print(f"num = {num}")

    square_dict = {n: n**2 for n in range(1,10) if n %2 ==0}
    print(f"square_dict = {square_dict}")

    keys = ["name", "job", "country"]
    values = ["Jane", "developer", "Canada"]
    person_dict = {k:v for k, v in zip(keys, values)}
    print(f"person_dict = {person_dict}")

    colors = ["red", "green", "blue"]
    color_dict = {c : len(c) for c in colors}
    print(f"colors = {color_dict}")

    basket = [["apple", "banana"], ["cherry", "date", "elderberry"]]
    basket_sub = [num for sublist in basket for num in sublist if len(num) > 5]
    print(f"basket_sub = {basket_sub}")

def insert_replace_delete():
    numbers = [1,2,3,7]
    print(f"original = {numbers}")
    numbers[3:3] = [4,5,6]
    print(f"insert = {numbers}")
    numbers[4:6] = [10, 20]
    print(f"replace = {numbers}")
    numbers[5:6] = []
    print(f"delete = {numbers}")

def list_exam():
    students_raw = [
        ["Alice", 85, 92, 78],
        ["Bob", 55, 60, 45],
        ["Charlie", 90, 88, 95],
        ["David", 40, 30, 50]
    ]
    print(f"original data = {students_raw}")
    # total 
    # 我們想要建立一個新的列表，裡面存放的是每個人的「總分」。
    totals = [sum(s[1:]) for s in students_raw]
    print(f"totals = {totals}")

    # 建立及格名單
    #「總分大於等於 180」才算及格。請建立一個字典，Key 是名字，Value 是總分，但只收錄及格的人。
    pass_list = {s[0]:sum(s[1:]) for s in students_raw if sum(s[1:]) > 180 }
    print(f"pass = {pass_list}")

    # 任務三：修正資料 (使用切片賦值)
    # 假設助教發現 David（索引 3）其實有參加補考，要把他的成績（從索引 1 開始的部分）更新為 [60, 65, 70]。
    students_raw[3][1:] = [60, 65, 70]
    print(f"new raw = {students_raw}")

    # student name upper
    name_upper = [s[0].upper() for s in students_raw ]
    print(f"name upper = {name_upper}")

    # show pass fail 
    status_with_score = {
        s[0].upper() : [sum(s[1:]), "Pass" if sum(s[1:]) >= 180 else "Fail"]
        for s in students_raw
    }
    print(f"status withc score = {status_with_score}")

    status_with_score2 = {
        s[0].upper() :{
            "score": sum(s[1:]), 
            "status": "PASS" if sum(s[1:]) >= 180 else "FAIL"
        }
        for s in students_raw
    }
    print(json.dumps(status_with_score2, indent=4))

def append_and_extend():
    a: list[Any] = ["a","b"]
    a.append("c")
    print(f"append \"c\" = {a}")
    a.append(["c", "d", "e"])
    print(f"append array = {a}")

    a.extend(["a", "p", "l", "e"])
    print(f"extend array={a}")
    a += ["1","2"]
    print(f"a+={a}")

    a.insert(1, "b")
    print(f"a.insert(1, \"b\") = {a}")

    a.remove("b")
    print(f"a.remove(\"b\") = {a}") # just remove first obj

    b = a.pop()
    print(f"a.pop = {b}")
    print(f"after a  = {a}")
    b = a.pop(2)
    print(f"a.pop(2) = {b}")
    print(f"after a  = {a}")
    print(f"len = {len(a)}")

    numbers = [2,6,4,5]
    print(f"len={len(numbers)}")
    print(f"min={min(numbers)}")
    print(f"max={max(numbers)}")
    print(f"sum={sum(numbers)}")

def package_unpackage():
    t = ("foo", "bar", "baz", "qux")

    I, O, U, T = t
    print(f"I={I}")
    print(f"O={O}")
    print(f"U={U}")
    print(f"T={T}")

    # ValueError: too many values to unpack (expected 3, got 4)
    # print(f"s1={s1}")
    # print(f"s2={s2}")
    # print(f"s3={s3}")



def list_practise():
    print("list_practise")
    # list_and_tuples()
    # list_and_range()
    # advance_operator()
    # insert_replace_delete()
    # list_exam()
    # append_and_extend()
    package_unpackage()
