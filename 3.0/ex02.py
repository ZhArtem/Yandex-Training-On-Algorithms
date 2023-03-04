"""
https://contest.yandex.ru/contest/45468/problems/2/


2. Красивая строка

Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Красотой строки назовем максимальное число идущих подряд одинаковых букв. (красота строки abcaabdddettq равна 3)

Сделайте данную вам строку как можно более красивой, если вы можете сделать не более k операций замены символа.

Формат ввода
В первой строке записано одно целое число k (0 ≤ k ≤ 10**9)

Во второй строке дана непустая строчка S (|S| ≤ 2 ⋅ 10**5). Строчка S состоит только из маленьких латинских букв.

Формат вывода
Выведите одно число — максимально возможную красоту строчки, которую можно получить.

Пример 1
Ввод	Вывод
2
abcaz
4
Пример 2
Ввод	Вывод
2
helto
3
"""


from string import ascii_lowercase


alphabet = ascii_lowercase
f = open('input.txt')
k = int(f.readline())
s = f.readline()
# k = int(input())
# s = input()
res = 0
for letter in alphabet:
    right = 0
    counter = k
    for left in range(len(s) - k):
        if left and s[left - 1] != letter:
            counter += 1
        while counter >= 0 and right < len(s):
            if s[right] != letter:
                if counter == 0:
                    break
                counter -= 1
            right += 1
        length = right - left
        if length > res:
            res = length
print(res)


