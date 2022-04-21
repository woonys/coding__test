'''
Runtime: 51 ms, faster than 82.33% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 13.9 MB, less than 87.00% of Python3 online submissions for Intersection of Two Arrays II.

1. 시간복잡도: O(m+n) -> 여기서 m, n은 nums1과 nums2 원소 수
why?
먼저 for문 돌면서 nums1에 있는 애들을 dictionary에 추가하고(개수도 추가 -> 중복될 수 있으니까 개수 넣어야 함!)
그 다음 nums2 원소 for문 돌면서 딕셔너리 안에 있는 값들을 하나씩 까내린다.
여기서 만약 dict value == 0이면 이미 중복된 애들 다 썼다는 뜻이니 패스.
따라서 시간복잡도는 O(m+n)

2. 공간 복잡도: O(m+n)
why?
ans 리스트 공간 -> m+n만큼 필요
dict key 공간 -> m(nums1 개수)개만큼 필요
평균적으로 O(m+n)
'''

from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        dic = defaultdict(int)
        for i in nums1:
            dic[i] += 1
        
        for j in nums2:
            if j in dic and dic[j] >= 1:
                dic[j] -=1
                ans.append(j)
        return ans