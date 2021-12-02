from sys import stdin
input = stdin.readline
 
nums = [2,7,9,3,1]
N = len(nums)
dp = [0] * N
 
dp[0], dp[1] = nums[0], max(nums[0], nums[1])

for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2]+nums[i])
print(dp[-1])