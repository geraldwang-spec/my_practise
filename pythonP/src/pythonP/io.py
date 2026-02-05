import os

def first_io():
    # file = open("dog_breads.txt", "rb")
    # print(f"{type(file)}")
    print(f"current path = {os.getcwd()}")
    print(f"{__file__}")

    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "dog_breads.txt")
    print(f"{open(file_path)}")
    print(f"{type(open(file_path))}")
    print(f"{open(file_path, "rb")}")
    print(f"{type(open(file_path, "rb"))}")
    print(f"{open(file_path, "wb")}")
    print(f"{type(open(file_path, "wb"))}")



def io_example():
    print("io_example")  
    first_io()
