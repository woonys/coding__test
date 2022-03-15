from collections import deque
def solution(progresses, speeds):
    queue = deque(progresses)
    speeds = deque(speeds)
    answer= []
    while queue != []:
        num = 0
        for i in range(len(queue)):
            queue[i] += speeds[i]
            print(queue, speeds)
        if queue[0] >= 100:
            while queue[0] >= 100:
                queue.popleft()
                speeds.popleft()
                num +=1
                if queue == deque([]):
                    answer.append(num)
                    return answer
        if num > 0:
            answer.append(num)
        print(answer)
    return answer

print(solution([93, 30, 55],[1, 30, 5]))

# 시간 복잡도: O(n**3)..매우 비효율적이나 테스트 케이스에서 제한 조건을 고려하면 최대 연산 횟수는 n당 100회로 제한되어있어 통과한듯...
# 공간 복잡도: O(N)
 
#다른 사람 풀이

'''
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds): // zip 함수: 함께 묶어서 튜플로 반환
        if len(Q)==0 or Q[-1][0]<-((p-100)//s): // why 100-p가 아니라 p-100? => math.ceil 쓰지 않기 위해
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
'''

'''
내 테케 결과
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.34ms, 10.1MB)
테스트 3 〉	통과 (0.98ms, 10.1MB)
테스트 4 〉	통과 (0.17ms, 10.1MB)
테스트 5 〉	통과 (0.02ms, 10.1MB)
테스트 6 〉	통과 (0.08ms, 10.3MB)
테스트 7 〉	통과 (0.70ms, 10.1MB)
테스트 8 〉	통과 (0.06ms, 10.1MB)
테스트 9 〉	통과 (0.55ms, 9.94MB)
테스트 10 〉통과 (0.64ms, 10.1MB)
테스트 11 〉통과 (0.02ms, 10.2MB)

다른 사람 풀이 테케 결과
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10MB)
테스트 7 〉	통과 (0.02ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)
테스트 10 〉통과 (0.03ms, 10.2MB)
테스트 11 〉통과 (0.01ms, 10.2MB)
'''