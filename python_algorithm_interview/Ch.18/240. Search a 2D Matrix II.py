'''
How to solve: bfs로 접근 -> 시간초과로 실패 / 답안 참고: 일일이 순회하면서 정답 찾는 방식

(답안 풀이)
Runtime: 148 ms, faster than 99.63% of Python3 online submissions for Search a 2D Matrix II.
Memory Usage: 20.7 MB, less than 12.20% of Python3 online submissions for Search a 2D Matrix II.

시간복잡도: O(log n): 한번 움직일 때마다 한 행 or 열을 통으로 날려버림 => 일일이 검사하지 않는다!
공간복잡도: O(1): in-place에서 해결
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # 책 답안 풀이
        if not matrix:
            return False
        
        row = 0
        col= len(matrix[0]) -1
        while row <=len(matrix)-1 and col >= 0:
            if target == matrix[row][col]:
                return True
            
            elif target < matrix[row][col]:
                col-=1
            elif target > matrix[row][col]:
                row+=1
        return False
        
        
        # my solution: bfs로 접근 => 시간초과
        max_width = len(matrix[0])
        max_height = len(matrix)
        #print(max_width, max_height, "max")
        #bfs
        queue = collections.deque()
        
        root = [0,0]
        queue.append(root)
        
        while queue:
            root = queue.popleft()
            now = matrix[root[0]][root[1]]
            if now == target:
                return True
            
            elif now < target:
                if root[0]+1 < max_height:
                    queue.append([root[0]+1, root[1]])
                
                if  root[1]+1 < max_width:
                    queue.append([root[0], root[1]+1])
            
        return False
        
        
        
        
#         max_width = len(matrix[0])
#         max_height = len(matrix)
        
#         #dfs
#         right = 1
#         down = 1
#         queue = collections.deque()
#         now = matrix[0][0]
#         #예외 케이스 처리
#         if now == target:
#             return True
        
#         def dfs(right, down, matrix):
#             root = matrix[0][0]
            
#             # 종료 조건
#             if root == target:
#                 return True
#             if right >= max_width:
#                 return
#             if down >= max_height:
#                 return
        
#             if root < target:
#                 dfs(right+1, down, matrix[])
                    

#                 if  down < max_height:
#                     queue.append(matrix[right][down])
#                     down+=1