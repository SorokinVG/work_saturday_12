def foo(a: int | float, b: int | float) -> int | float:
    """
    Функция, расчитывающая значение
    :param a: целое число, первое слагаемое
    :param b: целое число, второе слагаемое
    """
    c = a * b
    return (a + b) * c


def foo_2(a: int | float, b: int | float) -> int | float:
    """
    Функция, расчитывающая значение
    :param a: целое число, первое слагаемое
    :param b: целое число, второе слагаемое
    """
    c = a * b
    return (a - b) * c
