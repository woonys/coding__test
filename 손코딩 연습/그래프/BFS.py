from collections import deque

#기본 bfs
# queue를 활용해 두 개의 queue(데크)를 생성해 알고리즘 구현
def bfs(graph, startNode):
    visited, needVisited = list(), deque()
    
    needVisited.append(startNode)
    
    while needVisited:
        node = needVisited.popleft()
        if node not in visited:
            visited.append(node)
            needVisited.extend(graph[node])
    return visited
        

#최단경로 문제
def bfs_path(start):
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
