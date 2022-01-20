'''
1. my solution
Runtime: 883 ms, faster than 31.25% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 19.8 MB, less than 61.82% of Python3 online submissions for K Closest Points to Origin.
시간 복잡도: O(NlogN)
공간 복잡도: O(N)

2. Another solution(sorted + Euclidean Distance => sort 기준을 이렇게도 적용 가능하다!)
Runtime: 883 ms, faster than 31.25% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 19.8 MB, less than 61.82% of Python3 online submissions for K Closest Points to Origin.
'''

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
#1. my solution:         
        cmp = []
        for idx, point in enumerate(points):
            x = point[0]
            y = point[1]
            elem = [idx, math.sqrt((x**2)+(y**2))]
            cmp.append(elem)
        
        cmp.sort(key = lambda x: x[1])
        ans =[]
        for i in range(k):
            idx = cmp[i][0]
            ans.append(points[idx])
        
        return ans

#2. my solution
return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]