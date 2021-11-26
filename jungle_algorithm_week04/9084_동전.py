from sys import stdin

T = int(stdin.readline())
for i in range(T):
    N = int(stdin.readline())
    coins = list(map(int, stdin.readline().split())) # 오름차순으로 들어옴.
    money = int(stdin.readline())
    
    
    #만들 수 있는 가장 작은 금액: coins[0]임.
    D = [0] * 10001
    D[0] = 1
    for c in coins:
        for i in range(1, money+1):       
            if i-c >= 0:
                D[i] += D[i-c]                
    print(D[money])