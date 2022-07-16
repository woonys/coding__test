from bisect import bisect_left 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        How to solve: 답안 참고
        접근 방식은 동일하나 내 접근 방식에서 코드 구현이 미흡했음. 이진 탐색에 대한 이해도가 낮음.
        
        Runtime: 66 ms, faster than 46.05% of Python3 online submissions for Search a 2D Matrix.
        Memory Usage: 14.3 MB, less than 88.83% of Python3 online submissions for Search a 2D Matrix.
        
        '''
        r = bisect_left(matrix, target, key=lambda row: row[-1])  # or key=itemgetter(-1)
        return r < len(matrix) and matrix[r][bisect_left(matrix[r], target)] == target
            
        
#         m = len(matrix)
#         n = len(matrix[0])
        
#         first_entrance = []
#         for i in range(m):
#             first_entrance.append(matrix[i][0])
#         print("first_entrance is: ", first_entrance)
        
#         first_index = bisect_left(first_entrance, target) if (bisect_left(first_entrance, target) == target) else (bisect_left(first_entrance, target)-1)
#         print("first index: ", first_index)
#         if first_index >= m or first_index < 0:
#             return False
        
#         second_index = bisect_left(matrix[first_index], target)
#         if second_index >= m or second_index < 0:
#             return False
#         print("second index: ", second_index)
#         print("target is: ", matrix[first_index][second_index])
#         if matrix[first_index][second_index] == target:
#             return True
#         return False
        