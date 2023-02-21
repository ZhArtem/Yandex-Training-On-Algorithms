# https://contest.yandex.ru/contest/45468/problems/8/
#
#
# 8. Минимальный прямоугольник
#
#
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
#
#
# На клетчатой плоскости закрашено K клеток. Требуется найти минимальный по площади прямоугольник, со сторонами, параллельными линиям сетки, покрывающий все закрашенные клетки.
#
# Формат ввода
# Во входном файле, на первой строке, находится число K (1 ≤ K ≤ 100). На следующих K строках находятся пары чисел Xi и Yi – координаты закрашенных клеток (|Xi|, |Yi| ≤ 109).
#
# Формат вывода
# Выведите в выходной файл координаты левого нижнего и правого верхнего углов прямоугольника.


# k = int(input())
# x_list = []
# y_list = []
# for _ in range(k):
#     x, y = map(int, input().split())
#     x_list.append(x)
#     y_list.append(y)
# print(min(x_list), min(y_list), max(x_list), max(y_list))

k = int(input())
x_min = None
for _ in range(k):
    x, y = map(int, input().split())
    if x_min is None:
        x_min = x_max = x
        y_min = y_max = y
    if x < x_min:
        x_min = x
    if x > x_max:
        x_max = x
    if y < y_min:
        y_min = y
    if y > y_max:
        y_max = y

print(x_min, y_min, x_max, y_max)
