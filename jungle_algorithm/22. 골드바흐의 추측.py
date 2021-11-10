from sys import stdin

# n = int(stdin.readline())
# li = []
# for i in range(n):
#     a = int(stdin.readline())
#     li.append(a)
#
#
# def is_prime_num(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#
#     return True
#
# def prime_list(x): #x보다 작은 소수 집합을 리스트로 반환
#     temp_li = []
#     for i in range(2, x):
#        if is_prime_num(i) == True:
#            temp_li.append(i)
#     return temp_li
#
# def partition(x):
#     primeList = prime_list(x)
#     part_list = []
#     for i in primeList:
#         if (x-i) in primeList:
#             temp = [i, x-i]
#             temp.sort()
#             if temp in part_list:
#                 continue
#             else:
#                 part_list.append(temp)
#     diff_list = []
#     for i in part_list:
#         i1, i2 = i[0], i[1]
#         diff = abs(i1-i2)
#         diff_list.append(diff)
#
#     mi = min(diff_list)
#     min_index = diff_list.index(mi)
#     prime1, prime2 = part_list[min_index][0], part_list[min_index][1]
#     return f'{prime1} {prime2}'
#
# for i in li:
#     print(partition(i))
#
#시간 초과..


from sys import stdin

def Goldbach():
    check = [False]*2 + [True]*10000
    for i in range(2, 10001):
        if check[i] == True:
            for j in range(i+i, 10001, i):
                check[j] = False

    n = int(stdin.readline())
    li = []
    for i in range(n):
        a = int(stdin.readline())
        li.append(a)

    for i in li:
        A = i // 2
        B = A
        for _ in range(10000):
            if check[A] and check[B]:
                print(B, A)
                break
            A+=1
            B-=1


Goldbach()