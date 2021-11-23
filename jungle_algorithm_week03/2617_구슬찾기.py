#풀이 1: dfs 풀이

from sys import stdin

def find(dataset, start): # start보다 큰 수가 총 몇 개 있는지 찾는 함수
    global visited
    global check
    visited[start] = True
    for val in dataset[start]:
        if not visited[val]:
            check += 1
            find(dataset, val)

n, m = map(int, stdin.readline().split())

more = [[] for _ in range(n+1)]
less = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, stdin.readline().split())
    more[b].append(a)
    less[a].append(b)

visited = None
mid = int((n+1)/2)
count = 0
for i in range(1, n+1):
    visited = [False] * (n+1) # visit은 리셋을 해줘야 된다.
    check = 0
    find(more, i)
    if check >= mid:
        count +=1

    check = 0
    find(less, i)
    if check >= mid: # check는 값이 아니라 개수. 개수가 (n+1)/2개보다 많아야.
        count +=1

print(count)


#풀이 2: 플로이드 와샬

from sys import stdin

# 모든 구슬 관계 살펴보고 조건 확인하기

n, m  = map(int, stdin.readline().split())

arr = [[0] * (n+1) for _ in range(n+1)] # n*n 리스트 생성

for i in range(m):
    heavy, light = map(int, stdin.readline().split())
    arr[heavy][light] =1

# 플로이드 와샬 - 각 행렬간 연결관계를 표시 (1이면 대소 비교 O / 0이면 대소관계 없음)

for k in range(1, n+1):
    for j in range(1, n+1):
        for i in range(1, n+1):
            if arr[i][k] and arr[k][j]: # i-k가 연결되어 있고 k-j가 연결되어 있다면
                arr[i][j] = 1

ans = 0

for i in range(1, n+1):
    left_cnt = 0
    right_cnt = 0
    
    for j in range(1, n+1):
        if i == j:
            continue # 자기 자신이랑 비교하는 건 의미 X
        elif arr[i][j] == 1: # 현재 구슬(j)보다 무거운 구슬(i) 세기
            right_cnt += 1
        elif arr[j][i] == 1: # 현재 구슬(j)보다 가벼운 구슬(i) 세기
            left_cnt += 1
    if right_cnt >= (n+1)/2 or left_cnt >= (n+1)/2:
        ans +=1

print(ans)
    