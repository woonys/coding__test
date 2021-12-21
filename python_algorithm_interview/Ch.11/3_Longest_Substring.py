from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict()
        cur = ""
        max_ans = 0
        
        for i in s:
            if i not in dic.keys():
                dic[i] = 1
            else:
                if i in list(cur):
                    char_idx = list(cur).index(i)
                    cur_update = cur[char_idx+1:]
                    cur = cur_update
            
            cur += i
            max_ans = max(max_ans, len(cur))
        
        return max_ans