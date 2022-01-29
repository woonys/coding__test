'''
How to solve: 답안 참고
시간복잡도: O(NlogN) - heapq로 빼내고 n번 반복
공간복잡도: O(1) - 주어진 크기만큼
'''
import heapq
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        heap = []
        #키 역순, 인덱스 삽입
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))
        
        result = []
        
        # 키 역순, 인덱스 추출
        while heap:
            person = heapq.heappop(heap)
            #insert가 핵심이네..
            result.insert(person[1], [-person[0], person[1]])
        return result
        
#         ans = []
#         cnt = 0
#         heap = []
#         for i in people:
#             heapq.heappush(heap, [i[1],i]) # i[1] 작은 순으로 heap 정렬
        
#         while heap:
#             if heap[0][0] == 0:
#                 a = heapq.heappop(heap)
#                 ans.append(a[1])
#             for i in heap:
#                 if i[0] > 0:
#                     i[0] -= 1
#             heapq.heapify(heap)
#         return ans
            
            
            
        # people_cp = collections.deque(people)
        # people_cp.sort(key=lambda x:x[1])
        # ans = []
        # cnt = 0
        # while people_cp:
        #     if people_cp[0][1] == 0:
        #         ans.append(people_cp.popleft())
        #         cnt += 1
        #     else:
        #         if people_cp[0][1] - cnt <= 0:
                    
                
                    
                
            