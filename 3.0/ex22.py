"""
https://contest.yandex.ru/contest/45468/problems/22/


22. Кузнечик Ограничение времени	1 секунда Ограничение памяти	64Mb Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt У одного из студентов в комнате живёт кузнечик, который очень любит прыгать
по клетчатой одномерной доске. Длина доски — N клеток. К его сожалению, он умеет прыгать только на 1, 2, …,
k клеток вперёд.

Однажды студентам стало интересно, сколькими способами кузнечик может допрыгать из первой клетки до последней.
Помогите им ответить на этот вопрос.

Формат ввода
В первой и единственной строке входного файла записано два целых числа — N и k .

Формат вывода
Выведите одно число — количество способов, которыми кузнечик может допрыгать из первой клетки до последней.

Пример
Ввод	Вывод
8 2
21
"""


# n, k = map(int, input().split())
# dp = [0] * (n + k)
# for i in range(k + 1):
#     dp[i] = k
# for i in range(k + 1, n + k):
#     for j in range(1, k + 1):
#         dp[i] += dp[i - j]
#         print(i, j, dp[i])
# print(dp[n])


def func(n, k):
    a = []
    a.append(0)
    a.append(1)
    for i in range(1, n + 1):
        r = k
        if i < r:
            r = i
        a.append(0)
        for j in range(1, r + 1):
            a[i] = a[i] + a[i - j]
    return a[n]


n, k = map(int, input().split())
print(func(n, k))
