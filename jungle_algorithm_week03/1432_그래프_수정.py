from sys import stdin
import heapq


"""---내 풀이---"""

def topography_sort():
    hq = []
    k = n
    for i in range(1, n+1):
        if outdegree[i] == 0:
            heapq.heappush(hq, -i)

    while hq:
        now = -heapq.heappop(hq) # 튜플값 나온다.
        result[now] = k
        for l in graph[now]:
            outdegree[l] -= 1
            if outdegree[l] == 0:
                heapq.heappush(hq, -l)
        
        k-=1


n = int(stdin.readline())
nodes = []
for i in range(n):
    a = list(map(int, list(stdin.readline().strip())))
    nodes.append(a)

outdegree = [0] * (n+1)
result = [0] * (n+1)

graph = [[] for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        if nodes[i][j] == 1:
           graph[j+1].append(i+1)
           outdegree[i+1] +=1

topography_sort()

print(outdegree)
if result.count(0) > 1:
    print(-1)
else:
    ans = " ".join(map(str, result[1:]))
    print(ans)



# if sum(outdegree) != 0:
#     print(-1)
# else:
#     print(" ".join(map(str, result[1:])))



"""---진호형 풀이---"""

# def topology_sort():
#     q = []
#     for i in range(1, n+1):
#         if outdegree[i] == 0:
#             heapq.heappush(q, -i) # 그냥 해당 인덱스 값만 q에 넣는다. 첫 스타트 기준으로 3만.
#     N = n
#     while q:
#         now = -heapq.heappop(q) # now는 3
#         result[now] = N # 값 바꿔주고
#         for k in graph[now]:
#             outdegree[k] -= 1
#             if outdegree[k] == 0:
#                 heapq.heappush(q, -k)
#         N-=1

# n = int(stdin.readline())
# outdegree = [0] * (n+1)
# result = [0] * (n+1)

# graph = [[] for _ in range(n+1)]

# for i in range(1, n+1):
    