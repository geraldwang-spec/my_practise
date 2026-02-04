from typing import Any

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


def dictionaries_example():
    print("dictionaries_example")
    # basically()
    # class_example()
    # dict_operator()
    # enumerate_operator()
    # fromkeys_operator()
    exploring_dict()

    
