"""
Написать функцию multiply, которая принимает аргумент n.
и возвращает функцию closure, которая принимает аргумент x и возвращает x * n
"""


def multiply(n):
    def closure(x):
        return n * x

    return closure


if __name__ == "__main__":
    n_x = multiply(5)
    print(n_x(2))
