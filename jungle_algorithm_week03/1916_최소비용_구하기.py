from sys import stdin
import heapq

inf = 1e9


def dijkstra(n, start, end, cost_graph): # start: 출발 도시 / end: 도착 도시 / cost_graph: 비용 그래프
    q = []
    dist = [inf] * (n+1) # 시작점에서 각 점까지의 거리
    dist[start] = 0 # 출발점 기준 자신에서 자기까지 거리는 0
    heapq.heappush(q, [start, 0]) # 자신부터 출발하니 [start, 0]을 집어넣는다.
    
    while q:
        pos, cos = heapq.heappop(q) # 최소 비용인 애 뽑아냄 (pos: 해당 시점에서 출발점 & cos: 그때까지의 누적 최소 비용)
        for p, c in cost_graph[pos]: # cost_graph에서 pos(시작점)과 연결된 끝점(p)& 그에 드는 비용(c)을 뽑아서
            c += cos # 그 비용에다가 원래 시작점 비용을 더해준다. (비용 누적시킴)
            if c < dist[p]: #시작점에서 p점까지 거리가 c보다 크다면
                dist[p] = c
                heapq.heappush(q, [p, c])
    
    return dist[end]


n = int(stdin.readline())
m = int(stdin.readline())
cost_graph = [[] for _ in range(n+1)]

for i in range(m):
    start, end, cost = map(int, stdin.readline().split())
    cost_graph[start].append([end, cost]) # 2차원 배열이 아니라 1차원에다가 끝점을 배치 => 단방향 그래프이기 때문.

start_city, end_city = map(int, stdin.readline().split())

print(dijkstra(n, start_city, end_city, cost_graph))