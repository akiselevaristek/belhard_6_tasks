"""
Написать функцию bang, которая печатает "Boom"
Написать декоратор repeat_n_times, у которого есть параметр n.
Декоратор должен выполнить функцию bang n раз
"""
times = int(input("Сколько раз надо повторить функцию: "))


def decorator(n):
    def inner(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return inner


@decorator(times)
def some_func():
    print("Выполняется функция")


if __name__ == "__main__":
    some_func()