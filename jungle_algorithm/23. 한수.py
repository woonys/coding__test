from sys import stdin

N = int(stdin.readline())


def N_2(N):
    count = 99
    for i in range(100, N + 1):
        n_split = list(map(int, list(str(i))))
        if (n_split[0] - n_split[1]) == (n_split[1]-n_split[2]):
            count += 1
    return count


if N < 99:
    print(N)
elif N < 1000:
    print(N_2(N))
else:
    print(N_2(N-1))

