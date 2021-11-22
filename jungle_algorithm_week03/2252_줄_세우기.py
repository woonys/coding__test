from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
indegree = [0] * (n+1)
height = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, stdin.readline().split())
    height[a].append(b)
    indegree[b] += 1

def topology_sort():
    
    result = []
    q = deque()
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        
        for i in height[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=" ")
    return

print(topology_sort())