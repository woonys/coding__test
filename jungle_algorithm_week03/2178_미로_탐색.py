# from sys import stdin
# from collections import deque

# visit = [[False] * m+1 for _ in range(n+1)] # n*m 배열 생성
# queue = deque()


# # 이동해야 하니 dx, dy 만들기
# # 상 / 우 / 하 / 좌
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]


# def bfs(x, y):
#     # 1. 방문부터 하자.
#     visit[x][y] = True
    
#     for i in range(4): # 0: 상 1: 우 2: 하 3: 좌
#         nx = x + dx[i]
#         ny = y + dy[i]
#         queue.append([nx, ny])
#         if 1 <= nx < n+1 and 1 <= ny < m+1 and not visit[nx][ny]:
#             visited[nx][ny] = True
            
    
from sys import stdin
from collections import deque

# n, m 받아오기
n, m = map(int, stdin.readline().split())

graph = []
# 이차원 배열 생성
for i in range(n):
    a = list(stdin.readline().strip())
    graph.append(list(map(int, a)))


def bfs(x,y): # 어차피 x, y에 1, 1 넣어줄 예정
    # 이동 방향 정의
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 여기서는 굳이 visit이 필요가 없다 => 1이 있는 곳만 알아서 지나가기만 하면 됨.
            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 인덱스가 0 ~ n-1 / 0 ~ m-1 까지니까
                continue
            
            # 벽 만나면 진행 불가
            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1: # 1 만나면 위치 옮기고 append
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))