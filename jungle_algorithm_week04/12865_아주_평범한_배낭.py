from sys import stdin
input = stdin.readline

def solve():
    n, k = [int(x) for x in input().split()]
    table = [0] * (k+1)
    for _ in range(n):
        w, v = [int(x) for x in input().split()]
        if w > k:
            continue
        for j in range(k, 0, -1): # dp 테이블을 거꾸로 스캔
            if j + w <= k and table[j] != 0:
                table[j+w] = max(table[j+w], table[j] + v)
        table[w] = max(table[w], v)
    print(max(table))

solve()