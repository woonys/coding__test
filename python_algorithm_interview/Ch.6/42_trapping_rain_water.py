class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        #모든 바에다가 그 바에 담길 수 있는 왼/오 가장 높은 바를 체크 => i번째 바를 기준으로 i-1번째까지의 max를 비교
        maxleft, maxright = [0] * n, [0] * n
        
        for i in range(1, n):
            maxleft[i] = max(height[i-1], maxleft[i-1])
        
        for i in range(n-2, -1, -1):
            maxright[i] = max(height[i+1], maxright[i+1])
        
        ans = 0
        for i in range(n): # 모든 바를 돌면서 담길 수 있는 waterlevel을 체크
            waterlevel = min(maxleft[i], maxright[i])
            
            if waterlevel >= height[i]:
                ans += (waterlevel - height[i])
        return ans