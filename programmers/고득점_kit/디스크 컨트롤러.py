import heapq
def solution(jobs):
    ans = 0
    time = 0
    length = len(jobs)
    heapq.heapify(jobs) # 요청 시간 기준으로 정렬
    while jobs:
        heap = []
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