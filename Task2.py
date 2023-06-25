# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input("Введите длинну массива: "))
list_1 = list(range(1, n + 1))
x = int(input("Введите искомое число: "))
print(list_1)
print("x =", x)

def nearest_element(list_1, x):
    nearest = list_1[0]
    for i in list_1:
        diff = abs(i - x)
        if diff < abs(nearest - x):
            nearest = i
    return nearest

print("Ближайший элемент к", x, ":", nearest_element(list_1, x))


