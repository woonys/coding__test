from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)


# def num(n):
#     if len(n_list) > n-1:
#         return n_list[n-1]
#     else:
#         ans = (num(n-1)%15746 + num(n-2)%15746)% 15746
#         n_list.append(ans)
#         return ans


n = int(stdin.readline())
# print(num(a))

if n == 1:
    print(1)
else:
    n_list = [0] * (n)
    n_list[0] = 1
    n_list[1] = 2
    for i in range(1, n-1):
        n_list[i+1] = ((n_list[i-1] % 15746) + (n_list[i]%15746))%15746

    print(n_list[n-1])