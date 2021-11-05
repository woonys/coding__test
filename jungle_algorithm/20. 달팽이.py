# https://www.acmicpc.net/problem/2869
from sys import stdin
import math
A, B, V = map(int, stdin.readline().split())
# day = 1
# height = 0
# while height < V:
#     height += A
#     if height >= V:
#         break;
#     else:
#         height -= B
#         day +=1
# print(day) => 이렇게 짜면 시간 초과

day = math.ceil((V-A)/(A-B))+1
print(day)