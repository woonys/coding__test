a = int(input())
li = []
for i in range(a):
    t = input()
    li.append(t)


for i in li:
    total_count = 0
    count = 0
    for j in i:
        if j == "O":
            count +=1
        else:
            count = 0
        total_count += count
    print(total_count)


