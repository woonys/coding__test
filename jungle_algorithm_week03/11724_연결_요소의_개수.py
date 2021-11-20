from sys import stdin
from collections import Counter
n, m = map(int, stdin.readline().split())
graph = []
for i in range(m):
    a, b = map(int, stdin.readline().split())
    graph.append([a, b])

root = [i for i in range(n+1)]

def find_root(root, x):
    if root[x] != x:
        root[x] = find_root(root, root[x])
    return root[x]

def union(root, a, b):
    a_root = find_root(root, a)
    b_root = find_root(root, b)
    if a_root < b_root:
        root[b] = a_root
    else:
        root[a] = b_root

for a, b in graph:
    a_root = find_root(root, a)
    b_root = find_root(root, b)
    if a_root == b_root:
        continue
    else:
        union(root, a, b)

root = [find_root(root, i) for i in range(1, n+1)]

print(len(set(root[1:])))