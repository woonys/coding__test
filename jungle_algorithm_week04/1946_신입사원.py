from sys import stdin
input = stdin.readline

T = int(input())
ans = []
for i in range(T):
    sub = []
    N = int(input())
    for i in range(N):
        paper, interview = map(int, input().split())
        sub.append([paper, interview])

    sub.sort(key=lambda x: (x[0]))

    cnt = 1
    m = 0
    for i in range(1, len(sub)):
        if sub[m][1] > sub[i][1]:
            m = i
            cnt +=1
    print(cnt)
