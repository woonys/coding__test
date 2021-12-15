#코드리뷰) 혁주
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # not head 하나만 해도 된다. 왜냐하면 아래에서 even이 head.next = None이라도 while문을 돌지 않기 때문
        if not head or not head.next or not head.next.next: #속도향상을 위해서라면 조건들을 넣어주면 속도향상에 도움이 됨
            return head                                    
        odd = head
        even = head.next
        eHead = even
        
        
        while odd.next and even.next: #odd.next 대신 even을 쓰면 속도가 향상되는데, 
            odd.next = odd.next.next  #개인적인 생각으로는 변수로 선언을 해두고 그걸 사용하기 때문이라고 생각함(큰 차이 x)
            even.next = even.next.next
            
            odd = odd.next
            even = even.next
        odd.next = eHead
        return head
    
#discuss의 풀이중에 제일 이해가 쉽고 가독성 좋은 코드인것 같습니다!
'''재운 풀이 복기)전반적인 로직은 답안 없이 구현했으나, 노드를 홀/짝 따로 가리켰을 떄 각 노드를 어떻게 저장해야 좋을지 모르겠어서 계속 헤맸음. 

ex) head_odd, head_even 이런 식으로 홀/짝 각 노드가 다다음 노드를 가리키게 하고 나서(1->3->4->5 // 2->4->5) 1을 가리키고 있던 애를 3으로, 2를 가리키고 있던 애를 4로 옮기면 각각 노드들은  while 문이 다시 시작할 때 어디로 남아있게 되는지 감이 전혀 오지 않았던 게 문제.

답안을 참고하니 아직 포인터가 가리키고 있다는 개념을 잘 이해하지 못하고 있다는 것을 꺠달음.

여기서 odd/even은 따로 더미 없이 head의 홀/짝이 시작하는 노드를 가리키고 있음. (다만 eHead라고 해서 짝의 시작을 맨 처음으로 고정하는 포인터를 하나 생성. 이렇게 되면 head와 eHead는 전체 노드의 홀/짝 시작 노드를 가리키고 있는 상태에서 고정.)

이후에 odd와 even을 계속 다음 홀/짝 노드와 연결해주는데, (while문 내에서) while문이 끝나면 odd와 even은 각각 홀짝 노드의 끝을 가리키고 있음.
(*여기서 또 헷갈렸던게, while문이 다시 돌면 odd와 even은 새 값을 받는데 기존에 가리키고 있던 노드가 리셋되는 게 아닌가 생각함. 하지만 odd와 even을 옮기면 그 뒷 노드만 보는 것이고 앞에 head와 eHead가 전체 노드를 바라보고 있으니 중간에 odd와 even을 다음으로 넘겨도 head, eHead에 남아있음.*)

따라서 odd의 끝을 짝수 노드의 시작을 가리키고 있는 eHead에 연결해주면 한방에 완료.
'''