"""
Написать генератор fibonacci, который возвращает подряд значения числе Фибоначчи

Например:

fibonacci_gen = fibonacci()

next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 2
next(fibonacci_gen) -> 3
next(fibonacci_gen) -> 5
next(fibonacci_gen) -> 8
"""


def fibonacci():
    a = 1
    b = 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    fibonacci_gen = fibonacci()
    print(f'next(fibonacci_gen) -> {next(fibonacci_gen)}')
    print(f'next(fibonacci_gen) -> {next(fibonacci_gen)}')
    print(f'next(fibonacci_gen) -> {next(fibonacci_gen)}')
    print(f'next(fibonacci_gen) -> {next(fibonacci_gen)}')
    print(f'next(fibonacci_gen) -> {next(fibonacci_gen)}')
    print(f'next(fibonacci_gen) -> {next(fibonacci_gen)}')
    print(f'next(fibonacci_gen) -> {next(fibonacci_gen)}')

