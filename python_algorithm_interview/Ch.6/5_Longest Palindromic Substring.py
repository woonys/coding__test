class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투포인터 확장

        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        if len(s) < 2 or s == s[::-1]:
            return s
        result = ''
        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len) 
        return result




# My solution: 시간 초과..
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         longest_palindrom = ""
#         n = len(s)
#         max_length = 0
        
#         for i in range(n):
#             for j in range(i+1, n+1):
#                 candidate_s = s[i:j]
#                 if len(candidate_s) < max_length:
#                     continue
#                 if candidate_s == candidate_s[::-1]:
#                     s_leng = len(candidate_s)
#                     if s_leng > max_length:
#                         max_length = s_leng
#                         longest_palindrom = candidate_s
                
        
#         return longest_palindrom