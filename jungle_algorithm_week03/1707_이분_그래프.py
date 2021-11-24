#풀이 1: dfs

from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

def dfs(v, group): # v는 정점, group은 1번 그룹 이런 식으로.
    visited[v] = group # 방문한 노드에 group 할당
    for i in graph[v]:
        if visited[i] == 0: # 아직 안 가본 곳이면 방문
            if not dfs(i, -group): # 방문한 곳인데 그룹이 같으면 false => -group이니까 다른 그룹!
                return False
        elif visited[i] == visited[v]: # 혹은 맨 처음에 방문한 그룹과 인접 그룹이 같은 그룹이면 False
            return False
    return True

for _ in range(int(stdin.readline())):
    V, E = map(int, stdin.readline().split())
    graph = [[] for _ in range(V+1)] # 빈 그래프 생성
    visited = [0] * (V+1) # 방문한 정점 체크
    
    for _ in range(E): # 각 간선에 대해서
        a, b = map(int, stdin.readline().split())
        graph[a].append(b) # 무방향 그래프인데 임의로 방향을 지정..?
        graph[b].append(a)
    
    bigraph = True
    
    for i in range(1, V+1):
        if visited[i] == 0:
            bigraph = dfs(i, 1)
            if not bigraph:
                break
    print('YES' if bigraph else 'NO')
