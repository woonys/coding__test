class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrom = ""
        n = len(s)
        max_length = 0
        
        for i in range(n):
            for j in range(i+1, n+1):
                candidate_s = s[i:j]
                if len(candidate_s) < max_length:
                    continue
                if candidate_s == candidate_s[::-1]:
                    s_leng = len(candidate_s)
                    if s_leng > max_length:
                        max_length = s_leng
                        longest_palindrom = candidate_s
                
        
        return longest_palindrom