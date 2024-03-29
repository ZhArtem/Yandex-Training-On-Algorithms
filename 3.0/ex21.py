"""
https://contest.yandex.ru/contest/45468/problems/21/


21. Три единицы подряд Ограничение времени	1 секунда Ограничение памяти	64Mb Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt По данному числу N определите количество последовательностей из нулей и
единиц длины N, в которых никакие три единицы не стоят рядом.

Формат ввода
Во входном файле написано натуральное число N, не превосходящее 35.

Формат вывода
Выведите количество искомых последовательностей. Гарантируется, что ответ не превосходит 2**31-1.

Пример
Ввод	Вывод
1
2
"""


n = int(input())
dp = [-1] * (n + 2)
dp[0] = 1
dp[1] = 2
dp[2] = 4
for i in range(3, n + 2):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
print(dp[n])
