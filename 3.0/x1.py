stack = []
d_len = {}
names = {}
names_rev = {}
n = int(input())
res = []
for _ in range(n):
    s = input().split()
    if s[0] == 'add':
        num, name = s[1], s[2]
        num = int(num)


        if name not in names:
            names[name] = len(names)
            names_rev[len(names) - 1] = name
        for _ in range(num):
            stack.append(names[name])
        if name not in d_len:
            d_len[name] = 0
        d_len[name] += num

    if s[0] == 'get':
        name = s[1]
        if name in d_len:
            res.append(d_len[name])
        else:
            res.append(0)
    if s[0] == 'delete':
        for _ in range(int(s[1])):
            num = stack.pop()

            d_len[names_rev[num]] -= 1
print(*res, sep='\n')
    # print(names)
    # print(names_rev)
    # print(stack)
    # print(d_len)
    #
    # print()




