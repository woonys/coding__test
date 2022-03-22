from collections import deque
def solution(priorities, location):
    queue = deque()
    ans = list()
    for idx, val in enumerate(priorities):
        queue.append((val, idx))
    while queue:
        front = queue.popleft() 
        for i in queue:
            if front[0] < i[0]:
                queue.append(front)
                break
        if queue != deque([]):
            if queue[-1] == front:
                continue
            else:
                ans.append(front)
        else:
            ans.append(front)
            
    
    for idx, val in enumerate(ans):
        if val[1] == location:
            return idx+1

print(solution([1], 0))