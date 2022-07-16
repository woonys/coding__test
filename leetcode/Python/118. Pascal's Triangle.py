'''
답안 참고
1. 시간복잡도: O(numRows ** 2) => 파스칼 안에 하나의 원소로 들어가는 리스트의 개수(numRows) * 하나 리스트 만들 때 최대 numRows 길이만큼의 연산을 한다.
2. 공간복잡도: O(numRows ** 2 ) => res에 들어가는 총 원소 수의 평균 공간 복잡도는 numRows의 제곱

Runtime: 36 ms, faster than 70.62% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 13.9 MB, less than 68.26% of Python3 online submissions for Pascal's Triangle.
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            temp1 = res[-1] + [0]
            # print("temp1 is ", temp1)
            temp2 = [0] + res[-1]
            # print("temp2 is ", temp2)
            res.append([temp1[i] + temp2[i] for i in range(len(temp1))])
            # print("res: ", res)
        return res[:numRows]