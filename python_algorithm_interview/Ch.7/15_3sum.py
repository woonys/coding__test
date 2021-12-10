def threeSum(nums):
    nums.sort()
    
    ans = []
    
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i+1]:
            continue
        
        left = i+1
        right = len(nums)-1
        
        while left < right:
            threesum = nums[left] + nums[right] + nums[i]
            if threesum >0:
                right-=1
            elif threesum < 0:
                left +=1
            else:
                temp = [nums[i],nums[left], nums[right]]
                ans.append(temp)
                # 스킵 처리 => 이걸 생각 못함..
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
                left +=1
                right -=1
    return ans


    # my solution: 풀이 실패. 양 끝에서부터 출발.(O(N)이라 애초에 접근 방식이 틀림)
    # nums.sort()
    # left = 0
    # right = len(nums)-1
    # ans = []
    # while left < right:
    #     twosum = nums[left]+nums[right]
    #     for i in range(left+1, right): # left값과 right 값은 포함하지 않고 그 사이를 스캔
    #         if twosum + nums[i] == 0:
    #             temp = [nums[left], nums[right], nums[i]]
    #             temp.sort()
    #             if temp not in ans:
    #                 ans.append(temp)
    #     if twosum >=0:
    #         right-=1
    #     else:
    #         left +=1
    # return ans


nums= [-1,0,1,2,-1,-4,-2,-3,3,0,4]

print(threeSum(nums))