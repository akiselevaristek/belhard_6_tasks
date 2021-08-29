"""
Написать функцию get_even_number, которая принимает 1 аргумент - номер
четного числа и возвращает само четное число

Например:

- get_even_number(10) -> 20
- get_even_number(3) -> 6
"""


def get_even_number(x):
    result = x * 2
    return result


if __name__ == "__main__":
    print(get_even_number(-3))