x, y, w, h = map(int, input().split())

a1 = x
a2 = y
a3 = w-x
a4 = h-y

print(min(a1, a2, a3, a4))