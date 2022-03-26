'''
How to solve: my own solution
시간복잡도: O(nlogn) -> heapify 시간복잡도
'''

import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) >= 2:
        if scoville[0] >= K:
            return answer
        else:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            temp = first + 2*second
            heapq.heappush(scoville, temp)
            answer +=1
    if scoville[0] >= K:
        return answer
    return -1