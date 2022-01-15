class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Solution 1: sort -> 64ms
        # nums.sort(key=lambda x: -x)
        # return nums[k-1]
        
        # Solution 2: heap -> 106ms
        heap = []
        
        for i in nums:
            heapq.heappush(heap, -i)
        
        while k:
            k-=1
            a = heapq.heappop(heap)
        
        return -a