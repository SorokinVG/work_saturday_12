from src.mascs import foo, foo_2


def bar(x: int) -> list[int]:

    y = foo(2, 3)
    z = foo_2(10, 7)

    _list = [y,z,(y * z) + x]
    return _list
