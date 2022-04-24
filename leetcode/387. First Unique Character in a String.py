from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = defaultdict(list)
        
        for idx, val in enumerate(s):
            if dic[val] == []:
                dic[val].append(1)
                dic[val].append([idx])
            else: 
                dic[val][0] += 1
                dic[val][1].append(idx)
        
        for idx, val in enumerate(s):
            if dic[val][0] == 1:
                return idx
        return -1