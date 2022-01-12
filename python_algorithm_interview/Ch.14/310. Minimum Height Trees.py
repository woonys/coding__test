class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        # 리프 노드 추가
        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
        print(leaves)
        
        while n > 2:
            
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
            
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
        
            leaves = new_leaves
        return leaves
        

        
#         graph_table = [0] * (n)
#         graph = collections.defaultdict(list)
#         for u, v in edges:
#             graph[u].append(v)
#             graph_table[u] += 1
#             graph[v].append(u)
#             graph_table[v] += 1
#         #노드 가장 많은 애가 무조건 최소.
#         print(graph_table)
        
#         max_node_num = graph_table.index(max(graph_table))
#         ans_list = [max_node_num]
        
#         tot_minH = [float('inf')]
        
#         local_maxH = [0]
#         def measureH(start, height_path):
#             #종료 조건
#             if height_path > tot_minH[0]:
#                 return
            
#             if graph[start] == []:
#                 local_maxH[0] = max(local_maxH[0], height_path)
#                 return
           
#             #종료 조건 통과 시 height +1 (처음 값 0에서 출발)
#             height_path +=1
            
#             for i in graph[start]:
#                 measureH(i, height_path)
    
#         measureH(max_node_num, 0)
#         local_maxH[0] = 0
#         heap = []
#         heapq.heappush(())
        
        
        
        
        
            
            