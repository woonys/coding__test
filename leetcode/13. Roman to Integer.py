'''
시간복잡도: O(n) -> n은 문자열 s의 길이(글자 수)
한 칸씩 읽으면서 두 칸 읽어야 할 경우를 분기해서 체크

공간복잡도: O(1) -> 주어진 s의 메모리 공간 안에서 계속 길이를 줄여가며 진행
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        while len(s) > 0:
            if s[0] == "I":
                if len(s) >1 and s[1] == "V":
                    ans += 4
                    s = s[2:]
                elif len(s) >1 and s[1] == "X":
                    ans += 9
                    s = s[2:]
                else:
                    ans += 1
                    s = s[1:]
            elif s[0] == "X":
                if len(s) >1 and s[1] == "L":
                    ans += 40
                    s = s[2:]
                elif len(s) >1 and s[1] == "C":
                    ans += 90
                    s = s[2:]
                else:
                    ans += 10
                    s= s[1:]
            elif s[0] == "C":
                if len(s) >1 and s[1] == "D":
                    ans += 400
                    s = s[2:]
                    print(s)
                elif len(s) >1 and s[1] == "M":
                    ans += 900
                    s = s[2:]
                else:
                    ans += 100
                    s = s[1:]
            elif s[0] == "M":
                ans += 1000
                s = s[1:]
            elif s[0] == "D":
                ans += 500
                s = s[1:]
            elif s[0] == "L":
                ans += 50
                s = s[1:]
            elif s[0] == "V":
                ans += 5
                s = s[1:]
            
        return ans
                