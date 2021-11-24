from sys import stdin
from collections import deque

def bfs(bat):
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    visited = [[0] * m for _ in range(n)]
    cnt = 1
    for i in range(n):
        for j in range(m):
            if bat[i][j] == 1 and visited[i][j] ==0 :
                q.append([i, j])
                visited[i][j] = cnt
                while q:
                    x, y = q.popleft()
                    
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        
                        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and bat[nx][ny] == 1:
                            visited[nx][ny] = cnt
                            q.append([nx, ny])
                
                cnt += 1
    return cnt-1
                    

t = int(stdin.readline())
for i in range(t):
    m, n, k = map(int, stdin.readline().split())
    bat = [[0] * m for _ in range(n)]
    for j in range(k):
        y, x = map(int, stdin.readline().split())
        bat[x][y] = 1
    print(bfs(bat))
