'''
How to solve: 답안 참고
시간복잡도: O(2N): 전체 윈도우가 움직이는 건 O(N), 각 N번당 deque에서 최대 2번의 검사가 소요
공간복잡도: O(1): 상수 크기만큼의 공간 활용. 

'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # solution 2
        q = collections.deque()
        res = []
        
        for i, cur in enumerate(nums):
            while q and nums[q[-1]] < cur:
                q.pop()
            q.append(i)
            # remove first element if it's outside the window
            if q[0] == i - k:
                q.popleft()
            #if window has k elements add to results
            
            if i >= k-1:
                res.append(nums[q[0]])
        return res
            
        #solution 1: 시간초과
#         maxlist = []
#         leng = len(nums)
        
#         for i in range(leng - k + 1):
#             left_p = i
#             right_p = i+k-1
#             li = nums[left_p:right_p+1]
#             max_ = max(li)
#             maxlist.append(max_)
        
#         return maxlist

        