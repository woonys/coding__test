#풀이 1: 이중 for문 돌리기 => 60점

from sys import stdin

m, n, l = map(int, stdin.readline().split())
gun = list(map(int, stdin.readline().split()))
animal = [list(map(int, stdin.readline().split())) for _ in range(n)]

def distance(gun, animal):
    return (abs(gun-animal[0]) + animal[1])

count = 0
for i in gun:
    for j in animal[:]:
        if distance(i, j) <= l:
            count += 1
            print(j)
            animal.remove(j)


print(count)

#풀이 2: 