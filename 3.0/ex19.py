"""
https://contest.yandex.ru/contest/45468/problems/19/


19. Хипуй Ограничение времени	2 секунды Ограничение памяти	64Mb Ввод	стандартный ввод или input.txt Вывод
стандартный вывод или output.txt В этой задаче вам необходимо самостоятельно (не используя соответствующие классы и
функции стандартной библиотеки) организовать структуру данных Heap для хранения целых чисел, над которой определены
следующие операции: a) Insert(k) – добавить в Heap число k ; b) Extract достать из Heap наибольшее число (удалив его
при этом).

Формат ввода В первой строке содержится количество команд N (1 ≤ N ≤ 100000), далее следуют N команд, каждая в своей
строке. Команда может иметь формат: “0 <число>” или “1”, обозначающий, соответственно, операции Insert(<число>) и
Extract. Гарантируется, что при выполнении команды Extract в структуре находится по крайней мере один элемент.

Формат вывода
Для каждой команды извлечения необходимо отдельной строкой вывести число, полученное при выполнении команды Extract.

Пример 1
Ввод	Вывод
2
0 10000
1
10000
Пример 2
Ввод	Вывод
14
0 1
0 345
1
0 4346
1
0 2435
1
0 235
0 5
0 365
1
1
1
1
345
4346
2435
365
235
5
1
"""


def insert(arr, x):
    arr.append(x)
    pos = len(arr) - 1
    while pos and arr[pos] > arr[(pos - 1) // 2]:
        arr[pos], arr[(pos - 1) // 2] = arr[(pos - 1) // 2], arr[pos]
        pos = (pos - 1) // 2


def extract(arr):
    res = arr[0]
    arr[0] = arr[-1]
    pos = 0
    while pos * 2 + 1 < len(arr) - 1:
        max_son_index = pos * 2 + 1
        if arr[2 * pos + 2] > arr[2 * pos + 1]:
            max_son_index = pos * 2 + 2
        if arr[pos] < arr[max_son_index]:
            arr[pos], arr[max_son_index] = arr[max_son_index], arr[pos]
            pos = max_son_index
        else:
            break
    arr.pop()
    return res


heap = []
n = int(input())
for _ in range(n):
    s = input().split()
    if s[0] == '1':
        print(extract(heap))
    elif s[0] == '0':
        insert(heap, int(s[-1]))

