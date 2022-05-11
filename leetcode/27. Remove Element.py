class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt =  0
        for i in range(len(nums)-1, -1, -1):
            if val == nums[i]:
                nums.pop(i)
        return len(nums)
