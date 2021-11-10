#DP solution
from sys import stdin

n = int(stdin.readline())
W = []
for i in range(n):
    li = list(map(int, stdin.readline().split()))
    W.append(li)
citys = []

for i in range(n):
    citys.append(i)
for i in range(len(W)):
    W[i].insert(0, -1)
W.insert(0, [[-1]*len(W[i])])



#부분집합을 구하는 함수
def isIn (i, A):
    if ((A & (1 << (i-2)))) !=0:
        return True
    else:
        return False

#차집합을 구하는 함수
def diff(A, j):
    t = 1 << (j-2)
    return (A & (~t))

#A의 원소 개수를 count하는 함수
def count(A, n):
    count = 0
    for i in range(n):
        if ((A &(1 << i)) !=0):
            count +=1
    return count

#최종함수
def travel(W):
    n = len(W)-1
    size = 2**(n-1)
    D = [[0] * size for _ in range(n+1)]
    P = [[0] * size for _ in range(n+1)]
    for i in range(2, n+1):
        D[i][0] = W[i][1] #D[i][0]에서 [0]은 A가 공집합임을 뜻함 => W[i][1]은 vi에서 v1으로 갈때의 비용이니

    for k in range(1, n-1):
        A: int
        for A in range(1, size):
            if (count(A, n) == k):
                for i in range(2, n+1):
                    if not (isIn(i, A)):
                        D[i][A], P[i][A] = minimum(W, D, i, A)
    A = size -1
    D[1][A], P[1][A] = minimum(W, D, 1, A)
    return D, P

def minimum(W, D, i, A):
    minValue = 999
    minJ = 1
    n = len(W)-1
    for j in range(2, n+1):
        if (isIn(j, A)):
            if W[i][j] == 0:
                continue
            m = W[i][j] + D[j][diff(A, j)]
            if (minValue > m):
                minValue = m
                minJ = j
    return minValue, minJ



D, P = travel(W)
print(D[1][2**(len(W)-2)-1])











# my solution: 순열로 풀 때

from sys import stdin
from itertools import permutations


# 1을 출발점으로 고정
# n = int(stdin.readline())
# w = []
# for i in range(n):
#     li = list(map(int, stdin.readline().split()))
#     w.append(li)
# citys = []
# for i in range(2, n+1):
#     citys.append(i)












# total_path_list = []
# for i in permutations(citys):
#     pay_sum = 0
#     for j in range(len(i)-1):
#         start_city = 1
#         end_city = 1
#         from_city = i[j]
#         to_city = i[j+1]
#         if j == 0:
#             if w[start_city-1][from_city-1] == 0:
#                 break
#             else:
#                 pay_sum += w[start_city-1][from_city-1]
#         if w[from_city-1][to_city-1] == 0:
#             break
#         else:
#             pay_sum += w[from_city-1][to_city-1]
#         if j == len(i)-2:
#             if w[to_city-1][end_city-1] == 0:
#                 break
#             else:
#                 pay_sum += w[to_city-1][end_city-1]
#     total_path_list.append(pay_sum)
# print(min(total_path_list))