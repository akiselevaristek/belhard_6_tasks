"""
Написать функцию common_numbers, которая принимает 2 списка, которые содержат
целые числа.

Функция должна вернуть список общих чисел, который отсортирован по убыванию
"""
list_1 = [3, 6, 3, 7, 8, 1, 2, 6, 9]
list_2 = [2, 1, 6, 9, 6, 3, 89, 75, 0]


def common_numbers(a_lst: list, b_lst: list):
    result = []
    for i in a_lst:
        if i in b_lst and i not in result:
            result.append(i)
    for i in b_lst:
        if i in a_lst and i not in result:
            result.append(i)
    result.sort(reverse=True)
    return result


if __name__ == "__main__":
    print(common_numbers(list_1, list_2))
