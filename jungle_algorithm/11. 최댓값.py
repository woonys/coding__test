# https://www.acmicpc.net/problem/2562
li = []
for i in range(9):
    a = int(input())
    li.append(a)
k = max(li)
i = li.index(k)
print(k)
print(i+1)
