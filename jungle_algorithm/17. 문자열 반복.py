# https://www.acmicpc.net/problem/2675

a = int(input())

for i in range(a):
    num, case = map(str, input().split())
    sum= ""
    for i in case:
        sum += int(num)*i
    print(sum)