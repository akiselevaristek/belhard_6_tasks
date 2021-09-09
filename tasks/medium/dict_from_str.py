"""
Написать функцию dict_from_str, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}
"""
from collections import Counter

STR_VAL = 'python is the fastest-growing major programming language'


def dict_from_str(my_str: str):
    result = Counter(my_str)
    return result


if __name__ == "__main__":
    print(dict_from_str(STR_VAL))
