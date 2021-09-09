"""
Написать функцию triangular_sequence, которая принимает n и выводит
следующую последовательность

1
22
333
4444
55555
...

Например:

n = 3:
1
22
333

n = 6:
1
22
333
4444
55555
666666
"""


def triangular_sequence(n, i=''):
    if len(i) + 1 <= n:
        return triangular_sequence(n, i + str(n))
    else:
        return i


if __name__ == "__main__":
    print(triangular_sequence(9))
