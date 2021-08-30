"""
Написать рекурсивную функцию, которая будет вычислять сумму цифр целого числа

Можно пользоваться только функциями, операторами и условиями
"""


def num_sum(number, summa=0):
    if number >= 1:
        number, b = (divmod(number, 10))
        return num_sum(number, summa + b)
    else:
        return summa


if __name__ == "__main__":
    print(num_sum(12345))
