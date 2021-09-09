"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""


def get_even_number():
    current_value = 0
    while True:
        yield current_value
        current_value += 2


if __name__ == "__main__":
    even_gen = get_even_number()
    for i in even_gen:
        print(f'next(even_gen) -> {i}')
