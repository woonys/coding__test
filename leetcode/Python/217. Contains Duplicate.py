'''
시간 복잡도: O(n) -> items 쓰고 for문 돌면서 O(n)
공간 복잡도: O(n) -> counter 변수에 Counter 배정

Runtime: 482 ms, faster than 81.08% of Python3 online submissions for Contains Duplicate.
Memory Usage: 25.9 MB, less than 94.00% of Python3 online submissions for Contains Duplicate.
'''

from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for i in counter.items():
            if i[1] > 1:
                return True
        return False

# Solution 2
'''
Runtime: 489 ms, faster than 78.19% of Python3 online submissions for Contains Duplicate.
Memory Usage: 26 MB, less than 31.79% of Python3 online submissions for Contains Duplicate.
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

