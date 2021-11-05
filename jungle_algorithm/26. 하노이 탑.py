from sys import stdin

n = int(stdin.readline())

def move(start, to):
    print(start, to)

def hanoi(n, start, to, via):
    if n == 1:
        return move(start, to)
    else:
        hanoi(n-1, start, via, to)
        move(start, to)
        hanoi(n-1, via, to, start)

def hanoi_count(n):
    return (2**n -1)

if n > 20:
    print(hanoi_count(n))
else:
    print(hanoi_count(n))
    hanoi(n, 1, 3, 2)