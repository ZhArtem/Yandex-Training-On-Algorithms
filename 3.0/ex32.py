"""
https://contest.yandex.ru/contest/45468/problems/32/


32. Компоненты связности
Все языки	Python 3.6
Ограничение времени	2 секунды	5 секунд
Ограничение памяти	256Mb	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Дан неориентированный невзвешенный граф. Необходимо посчитать количество его компонент связности и вывести их.

Формат ввода
Во входном файле записано два числа N и M (0 < N ≤ 100000, 0 ≤ M ≤ 100000). В следующих M строках записаны по два
числа i и j (1 ≤ i, j ≤ N), которые означают, что вершины i и j соединены ребром.

Формат вывода
В первой строчке выходного файла выведите количество компонент связности. Далее выведите сами компоненты связности
в следующем формате: в первой строке количество вершин в компоненте, во второй - сами вершины в произвольном порядке.

Пример 1
Ввод	Вывод
6 4
3 1
1 2
5 4
2 3
3
3
1 2 3
2
4 5
1
6
Пример 2
Ввод	Вывод
6 4
4 2
1 4
6 4
3 6
2
5
1 2 3 4 6
1
5
"""
import sys
import threading

# print(sys.getrecursionlimit())
sys.setrecursionlimit(2**20)
threading.stack_size(2**20)
# thread = threading.Thread(target=your_code)
# thread.start()
# print(sys.getrecursionlimit())

def dfs(now, comp):
    visited[now] = comp
    for neig in graph[now]:
        if not visited[neig]:
            dfs(neig, comp)


# n, m = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# for _ in range(m):
#     f, s = map(int, input().split())
#     graph[f].append(s)
#     graph[s].append(f)

file = open('input.txt')
# print(f.readline())
n, m = map(int, file.readline().split())
graph = [[] for _ in range(n + 1)]
for line in file:
     f, s = map(int, line.split())
     graph[f].append(s)
     graph[s].append(f)


visited = [False for _ in range(n + 1)]
comp_now = 1
comps = []
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, comp_now)
        comps.append(comp_now)
        comp_now += 1

# print(visited)
# print(comps)


print(len(comps))
for comp in comps:
    ans = []
    cnt = 0
    for i in range(1, n + 1):
        if visited[i] == comp:
            cnt += 1
            ans.append(i)
    print(cnt)
    print(*ans)