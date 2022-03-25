'''
How to solve: my own solution

시간 복잡도: O(n^2) -> while 문 안에서 for문 돌기 때문
공간복잡도: O(n) -> 데크로 옮겨담는 과정
'''

from collections import deque
def solution(prices):
    answer = []
    queue = deque(prices)
    while queue:
        num = 0
        front = queue.popleft()
        if queue:
            for i in queue:
                if front <= i:
                    num += 1
                else:
                    num += 1
                    break
        answer.append(num)
    return answer