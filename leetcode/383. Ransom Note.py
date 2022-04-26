'''
Runtime: 113 ms, faster than 22.74% of Python3 online submissions for Ransom Note.
Memory Usage: 14.2 MB, less than 54.42% of Python3 online submissions for Ransom Note.
1. 시간복잡도: O(m+n) (m: ransomNote의 원소 수 & n: magazine의 원소 수)
why?
1. defaultdict에 각 원소 배정하기 -> O(m+n)
2. magazine dict에서 ransomNote 원소 하나씩 빼기 -> O(m)
3. ransomNote dict에서 각 원소 개수 세기 -> 모두 0이면 True / 하나라도 0이 아니면 False -> O(m)

2. 공간복잡도: O(1)
why?
ransomNote, magazine은 모두 알파벳으로 구성 -> dict에 배정되는 key는 최대 28개 & 각 key당 들어가는 val은 int.
=> O(1)의 공간복잡도를 갖는다.
'''

from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dic = defaultdict(int)
        ran_dic = defaultdict(int)
        
        for i in ransomNote:
            ran_dic[i] += 1
        for j in magazine:
            mag_dic[j] += 1
        
        for i in ransomNote:
            if mag_dic[i] == 0:
                return False
            else:
                mag_dic[i] -= 1
                ran_dic[i] -= 1
        for i in ransomNote:
            if ran_dic[i] != 0:
                return False
        return True
            