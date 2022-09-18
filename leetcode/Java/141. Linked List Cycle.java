public class 141. Linked List Cycle {
    public class Solution {
        public boolean hasCycle(ListNode head) {
            /*  Solution 1: HashSet에 Node를 저장
            시간 복잡도: O(n) - 전체 노드를 한 번씩 싹 훑어야 함. (n은 노드 길이)
            공간 복잡도: O(n) - hashSet에 지나간 노드 값을 일일이 저장한다.
            Runtime: 6 ms, faster than 16.48% of Java online submissions for Linked List Cycle.
            Memory Usage: 47.5 MB, less than 8.36% of Java online submissions for Linked List Cycle.
            */
            Set<ListNode> visited = new HashSet<>();
            if (head == null) {
                return false;
            }
            while(head != null) {
                if (head.next == null) {
                    return false;
                }
                
                if(visited.contains(head)) {
                    return true;
                }
                visited.add(head);
                head = head.next;
                }
             return true;
            /*
            Solution 2: fast & slow node를 사용
            증명: 나머지를 활용한 증명 -> https://math.stackexchange.com/questions/913499/proof-of-floyd-cycle-chasing-tortoise-and-hare
              
            시간 복잡도: O(n)
            공간 복잡도: O(1) -> 자료구조에 데이터를 담지 않고 노드로 이동만 한다.
            Runtime: 0 ms, faster than 100.00% of Java online submissions for Linked List Cycle.
            Memory Usage: 45.7 MB, less than 58.16% of Java online submissions for Linked List Cycle.
            */
            ListNode slow = head, fast = head;
            while(fast != null && fast.next != null) {
                slow = slow.next;
                fast = fast.next.next;
                
                if (slow == fast) {
                    return true;
                }
            }
            return false;
    
            }
        }
}
