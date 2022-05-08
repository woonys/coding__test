'''
카테고리: 정렬
난이도: Level2
시간복잡도: O(n) -> 여기서 n은 citations의 원소 수
공간복잡도: O(1)
'''

def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    
    for i in range(n):
        hIndex = n-i
        if citations[i] >= hIndex:
            answer = hIndex
            break
    return answer