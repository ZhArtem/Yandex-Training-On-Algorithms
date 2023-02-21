# https://contest.yandex.ru/contest/45468/problems/12/
#
# 12. Правильная скобочная последовательность
#
# Рассмотрим последовательность, состоящую из круглых, квадратных и фигурных скобок. Программа дожна определить, является ли данная скобочная последовательность правильной. Пустая последовательность явлется правильной. Если A – правильная, то последовательности (A), [A], {A} – правильные. Если A и B – правильные последовательности, то последовательность AB – правильная.
#
# Формат ввода
# В единственной строке записана скобочная последовательность, содержащая не более 100000 скобок.
#
# Формат вывода
# Если данная последовательность правильная, то программа должна вывести строку yes, иначе строку no.


s = input()
flag = ''
stack = []
for c in s:
    if c in '([{':
        stack.append(c)
    elif c == ')':
        if stack:
            if stack[-1] == '(':
                stack.pop()
            else:
                flag = 'no'
                break
        else:
            flag = 'no'
            break
    elif c == ']':
        if stack:
            if stack[-1] == '[':
                stack.pop()
            else:
                flag = 'no'
                break
        else:
            flag = 'no'
            break
    elif c == '}':
        if stack:
            if stack[-1] == '{':
                stack.pop()
            else:
                flag = 'no'
                break
        else:
            flag = 'no'
            break
if not flag:
    if stack:
        flag = 'no'
    else:
        flag = 'yes'
print(flag)

