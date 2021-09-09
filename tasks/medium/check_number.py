"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и 
False, если нет

Нельзя пользоваться операцией возведения в степень
"""
from math import sqrt


def check_number(n):
    n = sqrt(n)
    a, b = divmod(n, 10)
    if b == 0:
        check_number(n)
    return n


if __name__ == "__main__":
    print(check_number(16))
