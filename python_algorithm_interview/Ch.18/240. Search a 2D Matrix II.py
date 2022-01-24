'''
How to solve: bfs로 접근 -> 시간초과로 실패 -> visited 추가해서 해결 / 답안 참고: 일일이 순회하면서 정답 찾는 방식

(답안 풀이)
Runtime: 148 ms, faster than 99.63% of Python3 online submissions for Search a 2D Matrix II.
Memory Usage: 20.7 MB, less than 12.20% of Python3 online submissions for Search a 2D Matrix II.

시간복잡도: O(m+n): 한번 움직일 때마다 한 행 or 열을 통으로 날려버림 => 일일이 검사하지 않는다!
공간복잡도: O(1): in-place에서 해결

(내 풀이: bfs)
Runtime: 257 ms, faster than 29.47% of Python3 online submissions for Search a 2D Matrix II.
Memory Usage: 20.7 MB, less than 38.50% of Python3 online submissions for Search a 2D Matrix II.
시간복잡도: O(M*N) => 최악의 경우 O(N**2) => 전부 다 탐색해야 함.
공간복잡도: O(1) => in-place
'''

class Solution:
#     def binarySearch(self, target, arr):
#         start, end = 0, len(arr)-1
#         while start <= end:
#             mid = (start + end) //2
#             if target == arr[mid]:
#                 return True
            
#             if arr[mid] > target:
#                 end = mid-1
#             else:
#                 start = mid+1
        
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #solution 0: 이분탐색으로 접근해보기
        # for i in matrix:
        #     if i[0] > target:
        #         return False
        #     if self.binarySearch(target, i):
        #         return True
    
        
        
        
        
        
        
#----------------------------------
        # Solution 1: 답지 풀이
#         if not matrix:
#             return False
        
#         row = 0
#         col= len(matrix[0]) -1
#         while row <=len(matrix)-1 and col >= 0:
#             if target == matrix[row][col]:
#                 return True
            
#             elif target < matrix[row][col]:
#                 col-=1
#             elif target > matrix[row][col]:
#                 row+=1
#         return False
#----------------------------------
#         #my solution: bfs
        max_width = len(matrix[0])
        max_height = len(matrix)
        #print(max_width, max_height, "max")
        #bfs
        queue = collections.deque()
        
        root = [0,0]
        visited = [[False] * max_width for _ in range(max_height)]
        queue.append(root)
        
        while queue:
            root = queue.popleft()
            now = matrix[root[0]][root[1]]
            if now == target:
                return True
            
            elif now < target:
                if root[0]+1 < max_height:
                    if not visited[root[0]+1][root[1]]:
                        visited[root[0]+1][root[1]] = True
                        queue.append([root[0]+1, root[1]])
                
                if  root[1]+1 < max_width:
                    if not visited[root[0]][root[1]+1]:
                        visited[root[0]][root[1]+1] = True
                        queue.append([root[0], root[1]+1])
            
        return False
#----------------------------------
        
        
        # dfs 접근: 실패
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