'''
Runtime: 67 ms, faster than 51.00% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.4 MB, less than 68.53% of Python3 online submissions for Valid Anagram.
'''

from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dic = defaultdict(int)
        
        for i in s:
            s_dic[i] += 1
        
        for i in t:
            if s_dic[i] == 0:
                return False
            else:
                s_dic[i] -= 1
                
        for i in s:
            if s_dic[i] != 0:
                return False
        return True
            