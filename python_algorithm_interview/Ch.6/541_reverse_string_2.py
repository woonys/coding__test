class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        
        s = "".join(s)
        return s