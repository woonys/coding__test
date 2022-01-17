'''
- How to solve?: 답안
- 시간 복잡도: O(N**2) => but 정렬 없이 바로 합쳐도 되는 케이스는 바로 합체해줘서 최적화
- 공간 복잡도: O(N) => 주어진 케이스 별로

'''


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = start = ListNode(0)
        #start는 루트를 가리키고 cur은 정렬을 끝낸 연결리스트를 추가
        while head:
            while cur.next and cur.next.val < head.val: # 맨처음에 cur.next = None이므로 while문 통과
                cur = cur.next # 계속 이동
            
            cur.next, head.next, head = head, cur.next, head.next # 동시 할당! 순차가 아니라 동시 할당이라는 점이 중요
                      
            if head and cur.val > head.val: # 꼭 필요할 때만 맨 처음으로 돌아가고 그렇지 않으면 계속 진행
                cur = parent # 다시 루트 자리로 돌아가게!
        return parent.next