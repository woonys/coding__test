import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # Solution 1
        '''
        Runtime: 75 ms, faster than 66.82% of Python3 online submissions for Maximum Product of Two Elements in an Array.
        Memory Usage: 14 MB, less than 47.72% of Python3 online submissions for Maximum Product of Two Elements in an Array.

        시간복잡도: O(NlogN) - heap에 삽입하는데 드는 시간복잡도: logN & for문 돌면서 드는 시간: N -> NlogN
        공간복잡도: O(N)
        '''
        heap = []
        for i in nums:
            heapq.heappush(heap, -i)
        
        first = -heapq.heappop(heap)
        second = -heapq.heappop(heap)
        return (first-1)*(second-1)

        # Solution 2
        '''
        Runtime: 68 ms, faster than 75.62% of Python3 online submissions for Maximum Product of Two Elements in an Array.
        Memory Usage: 13.9 MB, less than 47.72% of Python3 online submissions for Maximum Product of Two Elements in an Array.
        
        시간복잡도: O(NlogN) - sort하는데 드는 시간복잡도
        공간복잡도: O(1) -> 새 공간을 쓰지 않고 기존 공간 활용
        '''
        nums.sort(reverse=True)
        first = nums[0]
        second = nums[1]
        return (first-1)*(second-1)