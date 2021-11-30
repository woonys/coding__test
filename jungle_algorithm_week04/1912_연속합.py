from sys import stdin

input = stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

dp = [0] * N
dp[0] = num_list[0]
for i in range(1, N):
    dp[i] =num_list[i] + (dp[i-1] if dp[i-1] > 0 else 0)

print(max(dp))