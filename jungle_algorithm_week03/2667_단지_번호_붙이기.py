from sys import stdin
from collections import deque

n = int(stdin.readline())

homes = [list(map(int, list(stdin.readline().strip()))) for _ in range(n)]
ans = [0]
visited = [[0] * n for _ in range(n)]

def bfs():
    vil_num = 1
    q = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(n):
        for j in range(n):
            if homes[i][j] != 0 and visited[i][j] == 0:
                cnt = 0
                q.append([i, j])
                visited[i][j] = vil_num
                while q:
                    x, y = q.popleft() 
                    
                    for m in range(4):
                        nx = x + dx[m] # 변수 조심! for 문 안에 for 문 돌릴 때 변수 다른 거 쓰기
                        ny = y + dy[m]
                        
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and homes[nx][ny] != 0:
                            visited[nx][ny] = vil_num
                            q.append([nx, ny])
                            cnt += 1
                            
                ans.extend([cnt])
                vil_num += 1
    return vil_num-1


vil_num = bfs()
ans.sort()
print(vil_num)
for i in ans[1:]:
    print(i)