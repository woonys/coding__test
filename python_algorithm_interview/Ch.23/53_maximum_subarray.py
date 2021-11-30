nums = [5,4,-1,7,8]
N = len(nums)
dp = [0] * N
dp[0] = nums[0]
for i in range(1, N):
    dp[i]= nums[i] + (dp[i-1] if dp[i-1] >= 0 else 0)
print(max(dp))