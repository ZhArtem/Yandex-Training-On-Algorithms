"""
https://contest.yandex.ru/contest/45468/problems/20/


20. Пирамидальная сортировка
Ограничение времени	2 секунды
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Отсортируйте данный массив. Используйте пирамидальную сортировку.

Формат ввода Первая строка входных данных содержит количество элементов в массиве N, N ≤ 105. Далее задаются N целых
чисел, не превосходящих по абсолютной величине 109.

Формат вывода
Выведите эти числа в порядке неубывания.

Пример 1
Ввод	Вывод
1
1
1
Пример 2
Ввод	Вывод
2
3 1
1 3
"""


def heap_sort(lst):
    build_max_heap(lst)
    for i in range(len(lst) - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        max_heapify(lst, index=0, size=i)


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def build_max_heap(lst):
    length = len(lst)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(lst, index=start, size=length)
        start = start - 1


def max_heapify(lst, index, size):
    l = left(index)
    r = right(index)
    if (l < size and lst[l] > lst[index]):
        largest = l
    else:
        largest = index
    if (r < size and lst[r] > lst[largest]):
        largest = r
    if (largest != index):
        lst[largest], lst[index] = lst[index], lst[largest]
        max_heapify(lst, largest, size)


n = int(input())
lst = [int(i) for i in input().split()]
heap_sort(lst)
print(*lst)
