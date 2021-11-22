from sys import stdin



def dfs(cnt, result, p, m, mul, div):
    
    global max_result
    global min_result

    if cnt == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    
    
    if p:
        dfs(cnt+1, result+num_list[cnt], p-1, m, mul, div)
    if m:
        dfs(cnt+1, result-num_list[cnt], p, m-1, mul, div)
    if mul:
        dfs(cnt+1, result*num_list[cnt], p, m, mul-1, div)
    if div:
        dfs(cnt+1, -(-result//num_list[cnt]) if result < 0 else result//num_list[cnt], p, m, mul, div-1)
    

n = int(stdin.readline())
num_list = list(map(int, stdin.readline().split()))
op = list(map(int, stdin.readline().split()))

max_result = -10**9
min_result = 10**9

dfs(1, num_list[0], op[0], op[1], op[2], op[3])

print(max_result)
print(min_result)
    
    