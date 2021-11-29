from sys import stdin
input = stdin.readline
N = int(input())
li = []
start = []
finish = []  
for i in range(N):
    s, f = map(int, input().split())
    li.append([s, f])

li.sort(key = lambda x: (x[1], x[0]))

ans = []

ans.append(li[0])
k = 0
for i in range(1, N):
    if li[k][1] <= li[i][0]:
        ans.append(li[i])
        k = i

print(len(ans))
