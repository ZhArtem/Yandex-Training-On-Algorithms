"""
https://contest.yandex.ru/contest/45468/problems/9/


9. Сумма в прямоугольнике Ограничение времени	3 секунды Ограничение памяти	256Mb Ввод	стандартный ввод или
input.txt Вывод	стандартный вывод или output.txt Вам необходимо ответить на запросы узнать сумму всех элементов
числовой матрицы N×M в прямоугольнике с левым верхним углом (x1, y1) и правым нижним (x2, y2)

Формат ввода В первой строке находится числа N, M размеры матрицы (1 ≤ N, M ≤ 1000) и K — количество запросов (1 ≤ K
≤ 100000). Каждая из следующих N строк содержит по M чисел`— элементы соответствующей строки матрицы (по модулю не
превосходят 1000). Последующие K строк содержат по 4 целых числа, разделенных пробелом x1 y1 x2 y2 — запрос на сумму
элементов матрице в прямоугольнике (1 ≤ x1 ≤ x2 ≤ N, 1 ≤ y1 ≤ y2 ≤ M)

Формат вывода Для каждого запроса на отдельной строке выведите его результат — сумму всех чисел в элементов матрице в
прямоугольнике (x1, y1), (x2, y2)

Пример
Ввод	Вывод
3 3 2
1 2 3
4 5 6
7 8 9
2 2 3 3
1 1 2 3
28
21
"""


n, m, k = map(int, input().split())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
prefix_matrix = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix_matrix[i][j] = prefix_matrix[i - 1][j] + prefix_matrix[i][j - 1] - prefix_matrix[i - 1][j - 1] + matrix[i - 1][j - 1]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefix_matrix[x2][y2] - prefix_matrix[x2][y1 - 1] - prefix_matrix[x1 - 1][y2] + prefix_matrix[x1 - 1][y1 - 1])