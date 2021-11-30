class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for j in range(1, n):
            # 1부터 출발
            dp[j+1]= dp[j] + dp[j-1]
        return dp[n]