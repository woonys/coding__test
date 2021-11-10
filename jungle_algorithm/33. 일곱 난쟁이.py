from sys import stdin
from itertools import combinations
dwarfs = []
for i in range(9):
    dwarf = int(stdin.readline())
    dwarfs.append(dwarf)

com = combinations(dwarfs, 7)

for i in com:
    if sum(i) == 100:
        a = list(i)
        a.sort()
        for j in a:
            print(j)
        break