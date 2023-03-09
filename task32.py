# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

# pytest -v tests\test_32.py


from random import randint

num_arr = [randint(-5, 20) for i in range(15)]
print(num_arr)
small_num = int(input("enter small_num: "))
large_num = int(input("enter large_num: "))


def is_in_mass(num_lst: list[int],
               min_num: int,
               max_num: int) -> list[int]:
    """Возвращает список индексов элементов списка, которые
    находятся в диапазоне [min_num,max_num] """
    res_arr = []
    for i in range(len(num_lst)):
        if min_num <= num_lst[i] <= max_num:
            res_arr.append(i)
    return res_arr


print(is_in_mass(num_arr, small_num, large_num))
