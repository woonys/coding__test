class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs.sort()
        stand = strs[0]
        for word in range(len(stand)):
            for i in strs:
                if i[word] != stand[word]:
                    return ans
            ans += stand[word]
        return ans
            