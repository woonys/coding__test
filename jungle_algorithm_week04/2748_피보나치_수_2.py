from sys import stdin
#DP로 풀려면?

n = int(stdin.readline())
D = [0, 1]

def fib_recur(n):
    if len(D) > n: # 저장되어 있는지 확인
        return D[n]
    else:
        fib = fib_recur(n-1) + fib_recur(n-2)
        D.append(fib)
        return fib

print(fib_recur(n))