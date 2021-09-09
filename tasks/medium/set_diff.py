"""
Написать функцию set_diff, которая принимает 4 аргумента: 3 множества и параметр
symmetric, который по умолчанию должен быть False.

Функция должна возвращать либо разность, либо симметричную разность
в зависимости от значения параметра symmetric
"""


def set_diff(set1: set, set2: set, set3: set, symmetric=False):
    if symmetric:
        result = set1 ^ set2 ^ set3
    else:
        result = set1 - set2 - set3
    return result


if __name__ == "__main__":
    one = {1, 4, 7, "a", "b", "c"}
    two = {1, 2, 5, "a", "g", "f"}
    three = {1, 3, 9, "a", "g", "l"}
    print(set_diff(one, two, three, True))
    print(set_diff(one, two, three))