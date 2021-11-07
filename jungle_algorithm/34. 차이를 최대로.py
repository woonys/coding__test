from sys import stdin
from itertools import permutations
a = int(stdin.readline())

li = list(map(int, stdin.readline().split()))

per = list(permutations(li))

def abs_max(list, k):
    total = []
    for i in list:
        sum_list = []
        for j in range(k-1):
            a, b = i[j], i[j+1]
            sum_list.append(abs(a-b))
        total.append(sum(sum_list))
    print(max(total))

if __name__ == "__main__":
    abs_max(per, a)

