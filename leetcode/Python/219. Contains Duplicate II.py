from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(list)
        for idx, val in enumerate(nums):
            dic[val].append(idx)
        
        set_nums = set(nums)
        for i in set(nums):
            if len(dic[i]) > 1:
                for j in range(len(dic[i])-1):
                    if dic[i][j+1] - dic[i][j] <= k:
                        return True
        return False