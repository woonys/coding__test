'''
How to solve: 답안 참고
시간복잡도: O(m+n)
    윈도우의 right가 움직이는게 n
    윈도우의 left가 움직이는 게 m
공간복잡도: O(m+n)
Runtime: 218 ms, faster than 26.49% of Python3 online submissions for Minimum Window Substring.
Memory Usage: 14.7 MB, less than 98.65% of Python3 online submissions for Minimum Window Substring.
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0
        
        for right, char in enumerate(s, 1):
            #print("before missing", missing)
            #print("need[char]", need[char])
            missing -= need[char] > 0 # 이거 무슨 의미지? if랑 같은 문법인가?
            #print('after missing', missing)
            
            need[char] -=1
            
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] +=1
                    left +=1
                
                if not end or right - left <= end - start:
                    start, end = left, right
                    need[s[left]]+=1
                    missing += 1
                    left +=1
        return s[start:end]