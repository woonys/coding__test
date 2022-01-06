class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        a = [i for i in range(1, n+1)]
        return list(combinations(a, k))
    
    #다른 풀이! dfs
    
    class Solution:
        def combine(self, n: int, k: int) -> List[List[int]]:
        li = [i for i in range(1, n+1)]
        ans = []
        path = []
        t = 0
        def dfs(li, path):
            #종료 조건
            if len(path) == k:
                ans.append(path)
                return
            
            for i in li:
                path_cp = path[:]
                path_cp.append(i)
                idx = li.index(i)
                if idx == len(li):
                    return
                dfs(li[idx+1:], path_cp)
                
        dfs(li, path)
        return ans