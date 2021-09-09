"""
Написать функцию biggest_dict, которая принимает словарь (необязательный аргумент)
и неограниченное количество аргументов вида ключ-значение.

Если был передан словарь, то она добавляет к нему все аргументы ключ-значение.
Если не был передан словарь, то создает новый, из аргументов ключ-значение она составляет
словарь и возвращает словарь
"""


def biggest_dict(d=None, **kwargs):
    if isinstance(d, dict):
        d.update(kwargs)
        result = d
    else:
        result = dict(kwargs)
    return result


if __name__ == "__main__":
    dict_my = {1: 2}
    print(biggest_dict(dict_my, key1='dscf', key2=2))
