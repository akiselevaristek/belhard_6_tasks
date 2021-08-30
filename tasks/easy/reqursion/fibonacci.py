"""
Написать рекурсивную функцию fibonacci, которая будет возвращать n-ый элемент
"""


def fibonacci(n):
    cur = 1
    if n > 2:
        cur = fibonacci(n - 1) + fibonacci(n - 2)
    return cur


if __name__ == "__main__":
    print(fibonacci(10))

