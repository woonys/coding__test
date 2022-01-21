'''
My solution
1. 시간복잡도: O(log n + n)
    처음에 인덱스 값 찾는데 n만큼 소요(length <= 5000이라서..)
2. 공간 복잡도: O(1)
    두 개의 리스트를 쓰긴하나 값을 변경하지는 않기에 값을 복사하지 않고 포인터 참조만 해도 가능
    
Runtime: 55 ms, faster than 36.90% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.7 MB, less than 23.31% of Python3 online submissions for Search in Rotated Sorted Array.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        length = len(nums)
        if length == 1:
            if nums[0] ==target:
                return 0
            else:
                return -1
            
        
        while nums[i] < nums[i+1]:
            i+=1
            if i+1 == length:
                break
        idx = i + 1
        
        #만약 모두 오름차순 정렬되어 있는 구조라면(idx == len(nums))
        if idx == length:
            ans = bisect.bisect_left(nums, target)
            
            
                
        #오름차순 정렬되어 있지 않은 상황
        else:
            list_before = nums[:idx]
            list_after = nums[idx:]
            #앞 리스트에 있을 때
            if nums[0] <= target <= nums[idx-1]:
                
                ans = bisect.bisect_left(list_before, target)
                print("before", ans)
                
            #뒷 리스트
            else:
                ans = bisect.bisect_left(list_after, target) + idx
                
                
        if ans >= length:
            return -1
        
        if nums[ans] == target:
            return ans
        else:
            return -1
        
        
            
            