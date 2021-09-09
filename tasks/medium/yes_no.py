"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(numbers: list):
    new_list = [numbers[0]]
    print(f"{numbers[0]} - No")
    for i in range(1, len(numbers)):
        if numbers[i] in new_list:
            print(f"{numbers[i]} - Yes")
        else:
            new_list.append(numbers[i])
            print(f"{numbers[i]} - No")


if __name__ == "__main__":
    yes_or_no([1, 4, 6, 4, 7, 9, 10, 22, 1, 4, 6, 7])
