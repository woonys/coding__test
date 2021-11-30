import heapq
people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
heap = []
for person in people:
    heapq.heappush(heap, [-person[0], person[1]])

result = []
while heap:
    person = heapq.heappop(heap)
    result.insert(person[1], [-person[0], person[1]])

print(result)