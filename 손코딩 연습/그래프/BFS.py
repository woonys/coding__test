from collections import deque

def bfs(start):
    queue = deque([(start, 0)]) # 큐에 (node, depth) 저장
    path = set([start])
    
    while queue:
        v, depth = queue.popleft() # deque.popleft는 O(1)
        if v == {종료 조건}:
            return depth
        for w in {w가 갈 수 있는 위치}:
            queue.append((w, depth + 1))
            path.add(w)
    return -1 # 두 노드 사이에 최단거리 존재하지 않음