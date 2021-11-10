from sys import stdin, setrecursionlimit
from typing import List

setrecursionlimit(100000)
N = int(stdin.readline())
safe_list = []

zone: List[List[int]] =[list(map(int, stdin.readline().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]  # 상하
dy = [0, -1, 0, 1]  # 좌우

def dfs(x, y, h):

    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]

        if (0 <= nx < N) and (0 <= ny < N) and not visit[nx][ny] and zone[nx][ny] > h: # 여기에도 zone[nx][ny] > h 가 들어 있어야 => 다음 재귀에서는 이 조건이 빠지니까
            visit[nx][ny] = True
            dfs(nx, ny, h) #이걸 return으로 작성하면 오류가 뜬다..! +1해서 값이 나온다.




ans = 1
for k in range(max(map(max, zone))):
    count = 0
    visit = [[False] * N for _ in range(N)] # h 바뀔 때마다 visit 리셋해줘야 함!
    for i in range(N):
        for j in range(N):
            if zone[i][j] > k and not visit[i][j]:
                count += 1
                visit[i][j] = True
                dfs(i, j, k)
    ans = max(ans, count)
print(ans)










# 오답 노트 때 작성할 것!
# 물의 높이가 1부터 h-1일때까지 각 케이스에 대한 safe_bool_list를 뽑아보자.

# for temp_h in range(h):
#     for i in range(len(safe_list)):
#         safe_dict = {}
#         for j in range(i):
#             if safe_list[i][j] < temp_h:
#                 safe_bool_list[i][j] = False
#             else:
#                 safe_bool_list[i][j] = True
#
#             try:
#                 for i in range(len(safe_bool_list)):
#                     for j in range(i):
#                         safe_dict[f'w{i}{j}'] = [safe_bool_list[i][j - 1], safe_bool_list[i][j + 1],
#                                                  safe_bool_list[i + 1][j], safe_bool_list[i - 1][j]]
#             except IndexError:
#                 pass
#     print(safe_bool_list)
# print(safe_dict)