from sys import stdin

num = int(stdin.readline())
pair = int(stdin.readline())

root = [i for i in range(num+1)]

def find_root(root, x):
    if root[x] != x:
        root[x] = find_root(root, root[x])
    return root[x]

def union(root, a, b):
    a = find_root(root, a)
    b = find_root(root, b)
    
    if a < b:
        root[b] = a
    elif a > b:
        root[a] = b
    else:
        return
    

for i in range(pair):
    a, b = map(int, stdin.readline().split())
    root_a = find_root(root, a)
    root_b = find_root(root, b)
    
    if root_a != root_b:
        union(root, root_a, root_b)
    else:
        continue

count = 0
for i in range(2, num + 1):
    find_root(root, i)
    if root[i] == 1:
        count+=1

print(count)