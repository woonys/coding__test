from sys import stdin
input = stdin.readline

N = int(stdin.readline())
A = list(map(int, input().split()))

D = [1] * (N)
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            D[i] = max(D[j]+1, D[i])
        else:
            continue

print(max(D))