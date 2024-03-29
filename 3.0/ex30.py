"""
30. НОП с восстановлением ответа
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Даны две последовательности, требуется найти и вывести их наибольшую общую подпоследовательность.

Формат ввода
В первой строке входных данных содержится число N – длина первой последовательности (1 ≤ N ≤ 1000). Во второй строке
заданы  члены первой последовательности (через пробел) – целые числа, не превосходящие 10000 по модулю.

В третьей строке записано число M – длина второй последовательности (1 ≤ M ≤ 1000). В четвертой строке задаются члены
второй    последовательности  (через пробел) –  целые числа, не превосходящие 10000 по модулю.

Формат вывода
Требуется вывести наибольшую общую подпоследовательность данных последовательностей, через пробел.

Пример 1
Ввод	Вывод
3
1 2 3
3
2 3 1
2 3
Пример 2
Ввод	Вывод
3
1 2 3
3
3 2 1
1
"""


def get_max_subsequence(n, a, m, b):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i] == b[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    i = n
    j = m
    res = []
    while i and j:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        elif dp[i][j] == dp[i - 1][j - 1] + 1:
            res.append(a[i])
            i -= 1
            j -= 1
    return res[::-1]


n = int(input())
seq1 = (0, )
seq1 += tuple(int(i) for i in input().split())
m = int(input())
seq2 = (0, )
seq2 += tuple(int(i) for i in input().split())

seq = get_max_subsequence(n, seq1, m, seq2)
print(*seq)