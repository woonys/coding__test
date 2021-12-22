class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict()
        for i in nums:
            if i not in dic.keys(): # 인자로 int를 적어줘야 if 문 없이도 작동함!
                dic[i] = 1
            else:
                dic[i] +=1
        ans = []
        dic_list = list(dic.items())
        dic_list.sort(key=lambda x: -x[1])
        for i in range(k):
            ans.append(dic_list[i][0])
        return ans
            