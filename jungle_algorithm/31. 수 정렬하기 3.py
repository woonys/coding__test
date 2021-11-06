from sys import stdin

N = int(stdin.readline())

pos = [0] * 10001

for i in range(N):
    num = int(stdin.readline())
    pos[num] += 1

for i in range(10001):
    if pos[i] !=0:
        for j in range(pos[i]):
            print(i)
