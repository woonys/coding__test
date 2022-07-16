'''
Runtime: 36 ms, faster than 92.86% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14 MB, less than 40.57% of Python3 online submissions for Merge Sorted Array.

시간복잡도: O(n) -> merged array를 합치는 과정이기 때문에 한 번 스캔만으로 가능
공간복잡도: O(1) -> 주어진 공간에 한해서 사용.
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        for i in range(n):
            k = i
            while nums1[k] <= nums2[0] and k < m:
                k+=1
            nums1.pop()
            nums1.insert(k, nums2[0])
            nums2 = nums2[1:]
            m+=1