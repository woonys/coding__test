N, X = map(int, input().split())
A = list(input().split())
li = []
for i in A:
    k = int(i)
    if k < X:
        li.append(i)
print(" ".join(li))
