from sys import stdin

# 2 < n <= 10000
a = int(stdin.readline())
li = []
for i in range(a):
    t = int(stdin.readline())
    li.append(t)

# prime list
def is_prime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def prime_list(x):
    p_li = []
    for i in range(2, x):
        if is_prime(i):
            p_li.append(i)
    return p_li


for i in li:
    print(i)
    ans_list = []
    for j in prime_list(i):
        print(prime_list(i))
        if (i - j) in prime_list(i):
            t = [j, i - j]
            t.sort()
            if t in ans_list:
                continue
            else:
                ans_list.append(t)

            if len(ans_list) > 1:
                temp = []
                for i in ans_list:
                    temp.append(abs(i[0] - i[1]))
                #print(ans_list[temp.index(min(temp))])
