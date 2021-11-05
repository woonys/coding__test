# https://www.acmicpc.net/problem/4344

a = int(input())
li = []
for i in range(a):
    t = list(map(int, input().split()))
    mean = sum(t[1:])/t[0]
    count = 0
    for j in t[1:]:
        if j > mean:
            count +=1
    print("%.3f%%" % (count / t[0] * 100.0))