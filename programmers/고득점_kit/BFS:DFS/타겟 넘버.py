'''
How to solve? 답안 참고
시간 복잡도: O(N^2)
공간 복잡도: O(N)
풀이 방법: BFS - 가능한 모든 답안 찾아낸 다음 하나씩 target과 비교
'''

# solution 1
def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []
        for leaf in leaves:
            tmp.append(leaf + num)
            tmp.append(leaf - num)
        leaves = tmp
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer

# solution 2: DFS

def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# solution 3: DFS -> 현실적인 DFS 풀이

answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer