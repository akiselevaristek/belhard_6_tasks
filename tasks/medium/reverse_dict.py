"""
Написать функцию reverse_dict, которая принимает словарь ключ-значение и
возвращает новый словарь, у которого ключи - значения первого, а значения -
ключи первого

Тело функции может состоять из одной строки!
"""


def reverse_dict(my_dict: dict):
    new_dict = dict(zip(my_dict.values(), my_dict.keys()))
    return new_dict


if __name__ == "__main__":
    print(reverse_dict({'a': 1, 'b': 2}))

