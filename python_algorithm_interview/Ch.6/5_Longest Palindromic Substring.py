
def longestPalindrome(s):
    longest_palindrom = ""
    n = len(s)
    # dp = [[0]* n for _ in range(n)]
    max_length = 0
    
    for i in range(n):
        for j in range(i+1, n+1):
            candidate_s = s[i:j]
            if candidate_s == candidate_s[::-1]:
                # dp[i][j].append(len(candidate_s), candidate_s)
                s_leng = len(candidate_s)
                if s_leng > max_length:
                    max_length = s_leng
                    longest_palindrom = candidate_s
    
    return longest_palindrom
        
s = "a"
print(longestPalindrome(s))
