class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. my solution
        # origin_list = []
        # for i in s:
        #     if i.isalnum() == True:
        #         origin_list.append(i)
        # origin_s = ""
        # origin_s = origin_s.join(origin_list).lower()
        #
        # s_reverse = origin_s[::-1]
        #
        # if origin_s == s_reverse:
        #     return True
        # else:
        #     return False

        # 2. 리스트로 변환
        # 2-1. 특수문자 전처리
        # strs = []
        # for char in s:
        #     if char.isalnum() == True:
        #         strs.append(char.lower())
        # # 2-2. 팰린드롬 판별
        # while len(strs) > 1:
        #     if strs.pop(0) != strs.pop():
        #         # pop()은 인덱스가 없으면 맨뒤에서부터 지움 => index로 0을 입력했으니 제일 앞을 빼오고 지우겠지
        #         return False
        #
        # return True

        # 3. 데크 자료형을 이용한 최적화
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True