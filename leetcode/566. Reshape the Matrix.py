'''
시간 복잡도: O(m*n) -> m, n은 행과 열 길이 => 행렬 원소 개수만큼의 시간 복잡도(O(N))
공간 복잡도: O(m*n) -> ans에 들어갈 공간 필요.
'''


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # r, c는 새로 만들어질 틀
        m = len(mat)
        n = len(mat[0])
        if r * c != m * n: return mat
        ans = [[0] * c for _ in range(r)] # 빈 칸으로 틀 만들고
        for i in range(m*n):
            # 몫과 나머지로 값을 배분한다!
            ans[i // c][i % c] = mat[i // n][i % n]
        return ans