class Solution:
    def reverseString(self, s: List[str]) -> None:
        # 1. my solution => 플랫폼 자체에서 제한 걸어둠
        # strs = "".join(s)
        # str_re = strs[::-1]
        # s = list(str_re)
        # return s

        # 2. pythonic way
        # return s.reverse()

        # 3. 투 포인터 스왑

        """
        Do not return anything, modify s in-place instead.
        = 리턴 없이 s 리스트 내부에서 직접 조작해라!
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1