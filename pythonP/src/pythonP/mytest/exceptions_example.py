from signal import raise_signal

def raise_example1()->None:
    number: int = 1
    assert (number > 5), f"qooo ({number})"
    print(f"number = {number}")


def raise_example()->None:
    number:int = 10
    if number > 5:
        raise Exception(f"the number should not exceed 5. ({number})")
    print(number)
    # raise Exception(f"testooo")

def exception_example()->None:
    print("exception example")
    # raise_example()
    raise_example1()
