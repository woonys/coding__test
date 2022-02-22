# https://programmers.co.kr/learn/courses/30/lessons/42576

'''
My solution
1) Time complexity: O(n) - for문 2번 병렬로 사용
2) Space complexity: O(n) - 딕셔너리에 2n 개 공간 사용
'''

from collections import defaultdict
def solution(participant, completion):
    dic = defaultdict(int)
    for i in participant:
        dic[i] += 1
    for comp in completion:
        if dic[comp] > 0:
            dic[comp] -= 1
            if dic[comp] == 0:
                del dic[comp]
    ans = list(dic.keys())
    return ans[0]

'''
Another Solution: collections.Counter 사용
사실상 동일한 로직이나 훨씬 간결한 풀이
'''

import collections
def solution(participant, completion):
    part = collections.Counter(participant) # 위의 풀이에서 defaultdict에 원소를 하나씩 for문으로 넣어주는 걸 counter로 해결
    comp = collections.Counter(completion)
    ans = part - comp
    return list(ans.keys())[0]
