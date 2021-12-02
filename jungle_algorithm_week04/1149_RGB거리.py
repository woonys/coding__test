from sys import stdin
input = stdin.readline
N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]

for i in range(3):
    dp[0][i] = W[0][i]

for i in range(1, N):
    for j in range(3):
        if j == 0: # red
            dp[i][j] = min(dp[i-1][1], dp[i-1][2]) + W[i][j]
        elif j == 1: # green
            dp[i][j] = min(dp[i-1][0], dp[i-1][2]) + W[i][j]
        elif j == 2: # blue
            dp[i][j] = min(dp[i-1][1], dp[i-1][0]) + W[i][j]

print(min(dp[N-1]))