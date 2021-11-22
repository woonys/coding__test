# 풀이 1: dfs

from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

n = int(stdin.readline())

tree = [[] for _ in range(n+1)] # 각 인덱스마다 연결된 노드를 트리에 저장
parents = [0] * (n+1) # 인덱스 0 제외하고
for i in range(n-1):
    a, b = map(int, stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(start, tree, parents):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i, tree, parents)
        # parents[i] !=0 인 애들은 건드릴 필요 없음.
dfs(1, tree, parents)

for i in parents[2:]:
    print(i)