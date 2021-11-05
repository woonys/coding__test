from sys import stdin
N = int(stdin.readline())
li = list(map(int, stdin.readline().split()))

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

count = 0
for i in li:
    if is_prime(i) is True:
        count +=1

print(count)