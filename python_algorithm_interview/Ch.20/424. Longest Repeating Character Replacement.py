class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = right = 0
        counts = collections.Counter()
        for right in range(1, len(s)+1):
            counts[s[right-1]] += 1
            max_char_n = counts.most_common(1)[0][1]
            
            # k 초과시 왼쪽 포인터 이동
            if right -left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
        return right - left
        
#         max_length = max_count = 0
        
#         count = defaultdict(int)
#         for right in range(len(s)):
#             count[s[right]] += 1
#             max_count = max(max_count, count[s[right]])
#             if max_length < k + max_count:
#                 max_length += 1
#             else:
#                 count[s[i-max_length]] -= 1
#         return max_length