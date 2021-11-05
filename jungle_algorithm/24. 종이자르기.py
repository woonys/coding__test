from sys import stdin

w, h = list(map(int, stdin.readline().split()))
count = int(stdin.readline())
li = []
for i in range(count):
    a = list(map(int, stdin.readline().split()))
    li.append(a)
list_w = [0, w]
list_h = [0, h]

for i in li:
    if i[0] == 0:
        list_h.append(i[1])
    else:
        list_w.append(i[1])
list_w.sort()
list_h.sort()

max_w = 0
max_h = 0

def find_max(x):
    compare_list = []
    for i in range(len(x)-1):
        a1, a2 = x[i], x[i+1]
        compare_list.append(a2-a1)
    max_x = max(compare_list)
    return max_x

print(find_max(list_w) * find_max(list_h))
