T = int(input())
li = []
for i in range(T):
    a, b = map(int, input().split())
    li.append([a, b])

for i in range(T):
    print(li[i][0] + li[i][1])

