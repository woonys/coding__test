from collections import deque
def bfs(start):
    queue = collections.deque([(start, 0)]) # 큐에 (node, depth) 저장
    