from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
coins = []

for i in range(N):
    a = int(input())
    if  a<=K:
        coins.append(a)

coins.reverse()
ans = K
cnt = 0
for i in coins:
    while  ans - i >=0:
        ans -= i
        cnt +=1

print(cnt)