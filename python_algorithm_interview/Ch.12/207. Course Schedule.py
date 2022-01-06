class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)
            
        
        visited = set()
        traced = set()
        
        def dfs(x):
            # 순환 구조이면 False
            if x in traced:
                return False
            if x in visited:
                return True
            
            traced.add(x)
            
            for y in graph[x]:
                if not dfs(y):
                    return False
            
            # 탐색 종료
            traced.remove(x)
            visited.add(x)
            
            return True
        
        for i in list(graph):
            if not dfs(i):
                return False
        return True
        