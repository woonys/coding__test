# from sys import stdin
# from collections import deque
# import heapq


# n = int(stdin.readline())

# miro = [list(map(int, stdin.readline().split())) for _ in range(n)]
# visited = [[False] * n for _ in range(n)]




# def bfs(x, y):
    
    
#     dx = [-1, 0, 1, 0]
#     dy = [0, -1, 0, 1]
    
#     q = deque()
#     black_room = list()
#     visited[x][y] = True
#     q.append((x, y))    
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx <n and 0 <= ny < n and not visited[nx][ny]:
#                 if miro[nx][ny] == 1:
#                     q.append((nx, ny))
#                 # 0 만나면 heappush
#                 heapq.heappush(q, )

"""--------------------------"""

from sys import stdin
import heapq

n = int(stdin.readline())

miro = [list(map(int, list(stdin.readline().strip()))) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def bfs():
    hq = []
    heapq.heappush(hq, [0, 0, 0]) # [0, 0, 0]: 시작점! 검은 벽돌 cnt / x좌표, y 좌표
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while hq:
        cnt, x, y = heapq.heappop(hq)
        if x == n-1 and y == n-1:
            return cnt
        if visited[x][y] == True:
            continue
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if miro[nx][ny] == 1:
                    heapq.heappush(hq, [cnt, nx, ny])
                elif miro[nx][ny] == 0:
                    heapq.heappush(hq, [cnt+1, nx, ny])
                    
print(bfs())         
                