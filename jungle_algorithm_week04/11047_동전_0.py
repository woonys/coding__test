from sys import stdin
""" 1번 풀이"""
input = stdin.readline

N, K = map(int, input().split())
coins = []

for i in range(N):
    a = int(input())
    if  a<=K:
        coins.append(a)

coins.reverse() # 얘는 문제 없음!
ans = K
cnt = 0

for i in coins:
    if ans >= i: # "=" 이거 하나 안 써서 계속 오답... 
        mod = ans // i
        ans %= i
        cnt += mod
        if ans == 0:
            break

print(cnt)



"""2번 풀이: dp는 여기서는 좋은 풀이가 아님! K 값이 최대 10억이라 리스트가 10억까지 만들어짐.."""

# dp = [1000000] * (K+1)

# dp[0] = 0

# for i in range(1, K+1):
#     for c in coins:
#         if i >= c:
#             dp[i] = min(dp[i-c]+1, dp[i])

# print(dp[K])