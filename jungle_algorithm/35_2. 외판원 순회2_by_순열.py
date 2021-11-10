from sys import stdin
from itertools import permutations

N = int(stdin.readline())

W = []
for i in range(N):
    a = list(map(int, stdin.readline().split()))
    W.append(a)
li = [i for i in range(1, N)]
#시작/끝 도시를 0으로 고정
per = permutations(li)
m = 999999999

def check(from_, to_):
    if W[from_][to_] == 0:
        return False
    return True

Min = 999999999
for p in per:
    if check(0, p[0]) == False:
        continue
    if check(p[-1], 0) == False:
        continue


    flag = True
    for i in range(len(p)-1):
        if check(p[i],p[i+1]) == False:
            flag = False
            break

    if flag == True:
        sum = W[0][p[0]] + W[p[-1]][0]
        for i in range(len(p)-1):
            sum += W[p[i]][p[i+1]]
        if Min > sum:
            Min = sum

print(Min)




##문제 발견: W[i][i]=0인게 들어가면 False라고 하는 것에 대해서는 고려되어 있지 X

###헌일님 풀이###
# from sys import stdin
# from itertools import permutations
#
# N = int(stdin.readline())
# W = []
# for i in range(N):
#     W.append(list(map(int, stdin.readline().split())))
# li = [i for i in range(1, N)]
# print(li)
# per = permutations(li)
#
#
# def check(fromm, to):
#     if W[fromm][to] == 0:
#         return False
#     return True
#
#
# result = 987654321
# for p in per:
#     p = list(p)
#     if check(0, p[0]) == False:
#         continue
#     if check(p[-1], 0) == False:
#         continue
#
#     flag = True
#     for i in range(len(p) - 1):
#         if check(p[i], p[i + 1]) == False:
#             flag = False
#             break
#
#     if flag is False:
#         continue
#
#     sum_ = W[0][p[0]] + W[p[-1]][0]
#     for i in range(len(p) - 1):
#         sum_ += W[p[i]][p[i + 1]]
#
#     result = min(result, sum_)
# print(result)