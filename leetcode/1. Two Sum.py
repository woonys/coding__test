from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(list)
        for idx, val in enumerate(nums):
            dic[val].append(idx)
        
        for idx, val in enumerate(nums):
            another = target-val
            if another in dic:
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
        
        # store = dict()
        # # store의 key에는 nums를, value에는 index를 저장
        # for idx, val in enumerate(nums):
        #     if target - val in store:
        #         return [store[target-val], idx]
        #     else:
        #         store[val] = idx
        # return []