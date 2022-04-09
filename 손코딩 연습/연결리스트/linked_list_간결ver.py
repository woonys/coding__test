class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
# 단일 Linked list 구현
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
    
    # 헤더부터 탐색해 뒤에 새로운 노드 추가
    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
    
    #모든 노드 값 출력
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
    
    # 노드 인덱스 알아내기
    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node
    
    # 삽입
    def add_node(self, index, value):
        new_node = Node(value) # 새 값을 노드로 감싼다.
        if index == 0: # 맨 앞에 넣으려고 하면
            new_node.next = self.head # new node 다음에 head를 연결
            self.head = new_node
            return
        node = self.get_node(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node
    
    #삭제
    def delete_node(self, index): # input으로 넣은 index에 위치하는 값을 삭제
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index-1)
        node.next = node.next.next
    
        