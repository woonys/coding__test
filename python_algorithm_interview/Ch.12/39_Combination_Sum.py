candidates = [2,3,6,7]
target = 7

# total = target
# result = []
# ans = []
        
# def dfs(csum, path):
#     if total == 0:
#         total_ans.append(path[:])
#         return
#     if total < 0:
#         return

#     for i in candidates:
#         if total - i >= 0:
#             path.append(i)
#             dfs(total-i, path)

        
# dfs(total, ans)
# print(total, ans)

'''
기본적인 조건은 잘 잡았음.
합 <0이면 종료, 합 == 0이면 중간에 구한 리스트를 result 리스트에 넣는 것 까지도.
dfs에 인자로 무엇을 넣는지가 명확하지 않았음.
자기 자신부터 시작해서 하위 원소까지 나열하는데,
DFS로 재귀 호출하되, dfs() 함수의 첫번째 파라미터는 합을 갱신할 csum
두 번째 파라미터는 순서(자기 자신을 포함)
세 번째 파라미터는 지금까지의 탐색 경로.
'''

result = []
def dfs(csum, index, path):
    # 종료 조건
    if csum < 0:
        return
    if csum == 0:
        result.append(path)
    
    for i in range(index, len(candidates)): # 여기서는 인덱스 값을 for문의 범위로 잡았다.
        dfs(csum-candidates[i], i, path + [candidates[i]])

dfs(target, 0, [])
print(result)