from sys import stdin
from collections import deque




n, m, v = map(int, stdin.readline().split()) 
graph = [[0] * (n+1) for _ in range(n+1)] # 인덱스 맞춰주려고 일부러 n+1개 만든다. 인덱스 0은 버린다.
visited = [0] * (n+1) # 아무 곳도 간 곳이 없으니 전부 0

for i in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a][b] = graph[b][a] = 1 # 값이 채워져 있으면 1 => 둘 사이는 연결되었다는 뜻



def bfs(start_node):
    visited[start_node] = 0 # 방문한 점을 0으로 표시 => 뒤에 하니까
    queue = deque()
    queue.append(start_node)
    
    while queue:
        start_node = queue.popleft()
        print(start_node, end=' ')
        for i in range(1, n+1):
            if (visited[i] == 1 and graph[start_node][i] == 1):
                queue.append(i)
                visited[i] = 0


def dfs(start_node):
    visited[start_node] = 1 # 방문한 점을 1로 표시 => dfs/bfs 둘이 같이 실행하니까!
    stack = []
    stack.append(start_node)
    
    while stack:
        start_node = stack.pop()
        print(start_node, end=" ")
        for i in range(1, n+1):
            if (visited[i] == 0 and graph[start_node][i] == 1):
                dfs(i)


dfs(v)
print()
bfs(v)