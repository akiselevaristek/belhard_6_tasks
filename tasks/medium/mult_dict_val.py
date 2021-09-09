"""
Написать функцию multiply_dict_values, которая принимает словарь SOME_DICT,
у которого ключи - строки, а значения - целые числа.

Необходимо, чтобы функция вернула результат умножения всех значений из словаря
"""
SOME_DICT = {str(val): val for val in range(1, 50, 3)}


def multiply_dict_values(my_dict: dict) -> dict:
    result = 1
    for value in my_dict.values():
        result = result * int(value)
    return result


if __name__ == "__main__":
    print(multiply_dict_values(SOME_DICT))