"""
https://contest.yandex.ru/contest/45468/problems/31/


31. Поиск в глубину
Все языки	Python 3.6
Ограничение времени	2 секунды	5 секунд
Ограничение памяти	256Mb	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Дан неориентированный граф, возможно, с петлями и кратными ребрами. Необходимо построить компоненту связности,
содержащую первую вершину.

Формат ввода
В первой строке записаны два целых числа N (1 ≤ N ≤ 10**3) и M (0 ≤ M ≤ 5 * 10**5) — количество вершин и ребер в графе.
В последующих M строках перечислены ребра — пары чисел, определяющие номера вершин, которые соединяют ребра.

Формат вывода
В первую строку выходного файла выведите число K — количество вершин в компоненте связности. Во вторую строку
выведите  K целых чисел — вершины компоненты связности, перечисленные в порядке возрастания номеров.

Пример
Ввод	Вывод
4 5
2 2
3 4
2 3
1 3
2 4

4
1 2 3 4
"""


def dfs(graph, visited, now, comp):
    visited[now] = comp
    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig, comp)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    f, s = map(int, input().split())
    graph[f].append(s)
    graph[s].append(f)

visited = [False for _ in range(n + 1)]
comp = 1
for i in range(1, n + 1):
    if not visited[i]:
        dfs(graph, visited, i, comp)
        comp += 1

ans = []
cnt = 0
for i in range(1, n + 1):
    if visited[i] == 1:
        cnt += 1
        ans.append(i)

print(cnt)
print(*ans)