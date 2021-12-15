'''
예외 케이스 처리하느라 죽는 줄.. 계속 예외케이스 뜬 것+ 시간 보면 좋은 풀이는 아님.
Runtime: 64 ms, faster than 5.59% of Python3 online submissions for Reverse Linked List II.
Memory Usage: 15.3 MB, less than 5.37% of Python3 online submissions for Reverse Linked List II.
Next challenges:
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy  = ListNode(0)
        total_dummy = dummy
        dummy.next = head
        total_dummy_next = head
        cnt = 0
        # 전체 값이 하나일 때
        if head.next == None:
            return head
        if left == right:
            return head
        # if head.next.next == None:
        #     return head
        
        while cnt != left-1:
            dummy = dummy.next
            cnt += 1
            
        dummy_tail= dummy.next
        before, cur = None, dummy.next
        after = cur.next
        
        
        while cnt != right:
            cur.next = before
            before = cur
            if after == None:
                dummy.next = before
                return total_dummy.next
                break
            cur = after
            after = after.next
            cnt += 1
        
        dummy.next = before
        dummy_tail.next = cur
        
        return total_dummy.next
        
        