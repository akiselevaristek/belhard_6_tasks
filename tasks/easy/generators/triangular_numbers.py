"""
Написать генератор triangular_numbers, который возвращает подряд числа
треугольные числа


Формула:

Tn = 1 / 2 * n * (n + 1)


Например:

tn_gen = triangular_numbers()

next(tn_gen) -> 1
next(tn_gen) -> 3
next(tn_gen) -> 6
next(tn_gen) -> 10
next(tn_gen) -> 15
next(tn_gen) -> 21
"""


def triangular_numbers():
    current_value = 1
    tn = 2
    while True:
        yield current_value
        current_value = current_value + tn
        tn += 1


if __name__ == "__main__":
    tn_gen = triangular_numbers()
    print(f'next(tn_gen) -> {next(tn_gen)}')
    print(f'next(tn_gen) -> {next(tn_gen)}')
    print(f'next(tn_gen) -> {next(tn_gen)}')
    print(f'next(tn_gen) -> {next(tn_gen)}')
    print(f'next(tn_gen) -> {next(tn_gen)}')
    print(f'next(tn_gen) -> {next(tn_gen)}')
    print(f'next(tn_gen) -> {next(tn_gen)}')