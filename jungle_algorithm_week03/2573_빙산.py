# from sys import stdin

# n, m = map(int, stdin.readline().split())
# place = []
# glac = []
# for i in range(n):
#     ice = list(map(int, stdin.readline().split()))
#     for j in range(m):
#         if ice[j] !=0:
#           place.append([i, j])  
#     glac.append(ice)

# def dfs(place):

#     dx = [-1, 0, 1, 0]
#     dy = [0, -1, 0, 1]

#     visited = [[False] * m for _ in range(n)]
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
        
#         while 

"""---------------------"""
# bfs 풀이

from sys import stdin
import copy
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def check_answer(): # 빙산이 2개로 분리되었는지 검사하는 함수
    visited = [[0] * m for _ in range(n)]
    q = deque()
    count = 1
    for i in range(n):
        for j in range(m):
            if count == 3:
                return True

            if ice[i][j] !=0 and visited[i][j] == 0:
                q.append([i, j]) # q에 append 먼저 해주고
                visited[i][j] = count # visited에 체크해주고
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <=ny < m:
                            if visited[nx][ny] == 0 and ice[nx][ny] !=0:
                                visited[nx][ny] = count
                                q.append([nx, ny])
                count +=1
    return False

n, m = map(int, stdin.readline().split())
ice = [list(map(int, stdin.readline().split())) for _ in range(n)]
time = 0
answer = 0

while True:
    if check_answer(): # 두개로 분리되었니? => 처음부터 True가 아니면 넘어가고
        answer = time
        break
    if ice.count([0] * m) == n: # 전부 다 얼음으로 바뀌면? 0 출력하면 되니까 그냥 break.
        break
    
    temp = copy.deepcopy(ice) # ice 맵을 하나 카피해와.
    for i in range(n):
        for j in range(m):
            if temp[i][j] !=0: # 빙산에 해당하면
                count = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if ice[nx][ny] == 0:
                            count +=1 # 마주하는 바다 개수를 센다
                temp[i][j] -= count # 실제로 깎는 건 temp고 ice는 아직 그대로 살아있음!
                if temp[i][j] < 0:
                    temp[i][j] = 0
    
    ice = copy.deepcopy(temp)
    time +=1

print(answer)