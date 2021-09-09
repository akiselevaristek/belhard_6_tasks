"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> 'Введите значение больше 1'
fibonacci(5)
1
2
3
5
8
"""
n = int(input("Введите n: "))


def fibonacci(num_count: int):
    a = b = 1
    if num_count <= 1:
        print('Введите значение больше 1')
    else:
        for i in range(0, num_count):
            a, b = b, a + b
            print(a)



if __name__ == "__main__":
    fibonacci(n)



