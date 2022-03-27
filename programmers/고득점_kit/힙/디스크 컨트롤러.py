'''
How to solve? 답안 참고
시간복잡도: O(N^2)
공간복잡도: O(n)

왜 못 풀었지? => time에 로직 분간이 명확하지 않았음. & 
배워야 할 스킬: start & end로 명확히 나눠서 로직 세우기
'''

import heapq
def solution(jobs):
    ans = 0
    start = -1
    end, i = 0, 0
    hq = []
    while len(jobs) > i:
        for job in jobs:
            if start < job[0] <= end:
                heapq.heappush(hq, (job[1], job[0]))
        if len(hq) > 0:
            work = heapq.heappop(hq)
            start = end
            end += work[0]
            ans += end-work[1]
            i += 1 # 작업 횟수
        else:
            end += 1
        
    return ans // len(jobs)

---- my solution ----
import heapq
def solution(jobs):
    ans = 0
    time = 0
    length = len(jobs)
    i = 0
    heap = []
    while len(jobs) > i:
        while jobs and time >= jobs[0][0]:
            job = heapq.heappop(jobs)
            heapq.heappush(heap, (job[1], job[0]))
        
        if heap != []:
            work = heapq.heappop(heap)
            ans += (time-work[1]+work[0])
            time += work[0]
        else:
            time += 1
        
    return ans // length
jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))


# import heapq
# def solution(jobs):
#     ans = 0
#     time = 0
#     length = len(jobs)
#     heapq.heapify(jobs) # 요청 시간 기준으로 정렬
#     while jobs:
#         heap = []
#         while jobs and time >= jobs[0][0]:
#             job = heapq.heappop(jobs)
#             heapq.heappush(heap, (job[1], job[0]))
        
#         if heap != []:
#             work = heapq.heappop(heap)
#             ans += (time-work[1]+work[0])
#             time += work[0]
#         else:
#             time += 1
        
#     return ans // length
# jobs = [[0, 3], [1, 9], [2, 6]]
# print(solution(jobs))