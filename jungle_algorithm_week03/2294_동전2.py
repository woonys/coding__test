from sys import stdin

n, k = map(int, stdin.readline().split())

coins = sorted([int(stdin.readline())for _ in range(n)])

# arr = [10001] * (k+1) # 배열의 모든 값을 10001로 => k의 최댓값이 10001이기 때문.

# arr[0] = 0

# for i in range(n):
#     for j in range(coins[i], k+1):
#         arr[j] = min(arr[j], arr[j-coins[i]]+1)

# arr[-1] = arr[-1] if arr[-1] != 10001 else -1
# print(arr[-1])

dp = [10001] * 10001
dp[0] = 0

for i in range(1, k+1):
    for c in coins: # 코인 하나씩 값을 뽑아온다.
        if i < c:
            break
        dp[i] = min(dp[i], dp[i-c]+1)

print(dp[k] if dp[k] != 10001 else -1)