"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""


def factorial():
    current_value = 1
    next_value = 2
    while True:
        yield current_value
        current_value = current_value * next_value
        next_value += 1


if __name__ == "__main__":
    factorial_gen = factorial()
    print(f'next(factorial_gen) -> {next(factorial_gen)}')
    print(f'next(factorial_gen) -> {next(factorial_gen)}')
    print(f'next(factorial_gen) -> {next(factorial_gen)}')
    print(f'next(factorial_gen) -> {next(factorial_gen)}')
    print(f'next(factorial_gen) -> {next(factorial_gen)}')
    print(f'next(factorial_gen) -> {next(factorial_gen)}')
    print(f'next(factorial_gen) -> {next(factorial_gen)}')


