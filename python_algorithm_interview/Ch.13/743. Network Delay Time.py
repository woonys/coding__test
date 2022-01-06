class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        weight = collections.defaultdict(dict)
        for u, v, w in times:
            weight[u][v] = w
        
        print(weight)
        heap = [(0, k)]
        dist= {}
        
        while heap:
            time, u = heapq.heappop(heap)
            if u not in dist:
                dist[u] = time
                for v in weight[u]:
                    heapq.heappush(heap, (dist[u] + weight[u][v], v))
        print(dist)
        return max(dist.values()) if len(dist) == n else -1