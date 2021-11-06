from sys import stdin
N = int(stdin.readline())

pos = [False] * 20000

for i in range(N):
    word = stdin.readline()
    word_length = len(word)
    if pos[word_length] == False:
        pos[word_length] = [word]
    else:
        pos[word_length].append(word)

for i in range(len(pos)):
    if pos[i] != False:
        pos[i] = list(set(pos[i]))
        pos[i].sort()
        for i in pos[i]:
            print(i, end="")


