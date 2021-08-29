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
    current_value = 1
    prew_value = 1
    while True:
        yield current_value
        current_value, prew_value = prew_value, current_value + prew_value



if __name__ == "__main__":
    fibonacci_gen = fibonacci()
    print(f'next(fibonacci_gen) -> {next(fibonacci_gen)}')
    print(f'next(fibonacci_gen) -> {next(fibonacci_gen)}')
    print(f'next(fibonacci_gen) -> {next(fibonacci_gen)}')
    print(f'next(fibonacci_gen) -> {next(fibonacci_gen)}')
    print(f'next(fibonacci_gen) -> {next(fibonacci_gen)}')
    print(f'next(fibonacci_gen) -> {next(fibonacci_gen)}')
    print(f'next(fibonacci_gen) -> {next(fibonacci_gen)}')
