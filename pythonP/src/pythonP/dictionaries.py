import sys
import timeit
from typing import Any

MLB_teams = {
    "Colorado": "Rockies",
    "Chicago": "White Sox",
    "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners",
} 


def basically():
    config = {
        "color" : "green",
        "width" : 42,
        "height" : 100,
        "font" : "Courier",
    }
    print(f"color = {config['color']}")
    config["font"] = "Helvetica"
    print(f"config[\"font\"] = \"Helvetica\" = {config['font']}")
    print(f"config = {config}")

class Number:
    def __init__(self, value) -> None:
       self.value = value

def class_example():
    n: Any = Number(42)
    print(f"n.value = {n.value}")
    print(f"n.__dict__ = {n.__dict__['value']}")
    n.name = "answer"
    print(f"n.__dict__ = {n.__dict__}")

def dict_operator():
    print(dict())
    d2 = dict(name = "Gemini", age = 2, city= "Mountain View")
    print(f"dict  example 2 = {d2}")
    base = {"a":1, "b":2}
    d3 = dict(base, b=99, c=3 )
    print(f"d3 = {d3}")
    kyes = ["x", "y", "z"]
    values = [10,24,30]
    d4 = dict(zip(kyes, values))
    print(f"d4 = {d4}")

def enumerate_operator():
    fruits = ["蘋果", "香蕉", "芒果"]
    for i, fruit in enumerate(fruits):
        print(f"count:{i}, value: {fruit}")

    names = ["Alice", "Bob", "Charlie"]
    scores = [90, 80, 70]
    result = {name: score for name, score in enumerate(zip(names, scores))}
    print(f"result = {result}")

def fromkeys_operator():
    # 把一個 List 當作預設值傳給 fromkeys()，所有的 Key 都會共享同一個 List 的記憶體位址。
    users = ["Alice", "Bob", "Charlie"]
    status = dict.fromkeys(users, False)
    print(f"user = {status}")
    print(f"data = {dict.fromkeys("ABC", 0)}")

def exploring_dict():
    inventory = {"apple": 100, "orange": 80, "banana": 100}
    print(f"orignal = {inventory}")
    print(f"inventory.get(\"apple\") = {inventory.get("apple")}")
    print(f"get mango = {inventory.get("mango", 0)}")
    print(f"orignal = {inventory}")
    print(f"inventory.values() = {inventory.values()}")
    print(f"inventory.kyes() = {inventory.keys()}")
    print(f"inventory.items() = {inventory.items()}")

    config = {
        "color": "green",
        "width": 42,
        "height": 100,
        "font": "Courier",
    }
    inventory.update(config)
    print(f"update = {inventory}")

    print(f"pop[\"apple\"] = {inventory.pop("apple")}")
    print(f"orignal = {inventory}")
    print(f"popitem = {inventory.popitem()}")
    print(f"orignal = {inventory}")
    print(f"clear = {inventory.clear()}")
    print(f"orignal = {inventory}")

def membership_in_not_in():
    print(f"Milwaukee = {'Milwaukee' in MLB_teams}")
    print(f"Indianapolis = {"Indianapolis" in MLB_teams}")
    print(f"Indianapolis = {"Indianapolis" not in MLB_teams}")

    print(f"Milwaukee = {'Milwaukee' in MLB_teams.keys()}")
    print(f"Indianapolis = {"Indianapolis" in MLB_teams.keys()}")
    print(f"Indianapolis = {"Indianapolis" not in MLB_teams.keys()}")

    time_in_dict = timeit.timeit('"Milwaukee" in MLB_teams', globals=globals(), number=1000000)
    time_in_keys = timeit.timeit(
        '"Milwaukee" in MLB_teams.keys()', globals=globals(), number=1000000
    )
    time_not_in_dict = timeit.timeit(
        '"Indianapolis" in MLB_teams', globals=globals(), number=1000000
    )
    time_not_in_keys = timeit.timeit(
        '"Indianapolis" in MLB_teams.keys()', globals=globals(), number=1000000
    )
    
    print(
        f"{time_in_dict     = } seconds",
        f"{time_in_keys     = } seconds",
        f"{time_not_in_dict = } seconds",
        f"{time_not_in_keys = } seconds",
        sep="\n",
    )



def sort_operator():
    students = {
        "Alice": 89.5,
        "Bob": 76.0,
        "Charlie": 92.3,
        "Diana": 84.7,
        "Ethan": 88.9,
        "Fiona": 95.6,
        "George": 73.4,
        "Hannah": 81.2,
    }
    print(f"students = {students}")
    print(f"students sort = {dict(sorted(students.items(), key=lambda item: item[1]))}")
    print(f"students sort = {dict(sorted(students.items(), key=lambda item: item[0]))}")
    print(f"students sort2 = {dict(sorted(students.items(), key=lambda x: (-x[1], x[0])))}")

def dict_practise():
    names = ['手機', '電腦', '耳機', '測試品']
    stocks = [15, 8, 0]

    print(dict(sorted(filter(lambda x: x[1],  zip(names, stocks)), key=lambda x: x[1], reverse=True)))

def compare_list_generator():
    n = 10000000
    my_list =  [i for i in range(n)]
    list_size = sys.getsizeof(my_list) / 1024

    my_gen = (i for i in range(n))
    gen_size = sys.getsizeof(my_gen) / 1024

    print(f"list size = {list_size:2f} KB")
    print(f"gen size = {gen_size:2f} KB")


def dictionaries_example():
    print("dictionaries_example")
    # basically()
    # class_example()
    # dict_operator()
    # enumerate_operator()
    # fromkeys_operator()
    # exploring_dict()
    # sort_operator()
    # dict_practise()
    # membership_in_not_in()
    compare_list_generator()

    
