from collections import defaultdict
class Solution:
    #Solution 1
        '''
        Runtime: 67 ms, faster than 83.33% of Python3 online submissions for Two Sum.
        Memory Usage: 16.2 MB, less than 9.74% of Python3 online submissions for Two Sum.
        '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(list)
        for idx, val in enumerate(nums):
            dic[val].append(idx)
        
        for idx, val in enumerate(nums):
            another = target-val
            if another in dic: #O(1)
                # 원소가 하나일 때
                if len(dic[another]) ==1:
                    another_idx = dic[another][0]
                    if another_idx == idx:
                        continue
                    return [idx, another_idx]
                
                #원소가 둘 일 때
                else:
                    dic[another].remove(idx)
                    another_idx = dic[another][0]
                    return [idx, another_idx]
        
        # Solution 2
        '''
        Runtime: 88 ms, faster than 62.92% of Python3 online submissions for Two Sum.
        Memory Usage: 15.1 MB, less than 50.82% of Python3 online submissions for Two Sum.
        
        Q: 왜 sol2가 sol1보다 느리지?
        
        '''
        
        store = dict()
        # store의 key에는 nums를, value에는 index를 저장
        for idx, val in enumerate(nums):
            if target - val in store: #O(1) -> 딕셔너리니까
                return [store[target-val], idx]
            else:
                store[val] = idx # 없으면 값 추가하고
        return []