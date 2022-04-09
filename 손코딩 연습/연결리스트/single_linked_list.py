from dataclasses import dataclass


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
# Singly linked list class

class singly_linked_list(object):
    def __init__(self):
        self.head = None
        self.count = 0
    
    # Add new node at the end of the linked list -> 끝에 배치해야 하니 O(n)
    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    
    # return the first index of data in the linked list
    def getdataIndex(self, data):
        curn = self.head
        idx = 0
        while curn:
            if curn.data == data:
                return idx
            curn = curn.next
            idx += 1
        # 없으면 -1
        return -1

    def Insert_Node_at_Index(self, idx, node):
        """
        node는 3 가지 방식으로 추가될 수 있음.
        1) 연결리스트 맨 앞에
        2) 주어진 인덱스에서
        3) 연결리스트 맨 뒤에
        """
        curn = self.head
        prevn = None
        cur_i = 0
        
        # (1) Add 0 index
        if idx == 0:
            if self.head:
                nextn = self.head
                self.head = node
                self.head.next = nextn
            else:
                self.head = node
        else:
            #(2) Add at the given index &
            #(3) At the end of the linked list
            while cur_i < idx:
                if curn:
                    prevn = curn
                    curn = curn.next
                else:
                    break
                cur_i += 1
            if cur_i == idx:
                node.next = curn
                prevn.next = node
            else:
                return -1
    
    # Add new node before the given data
    def Insert_Node_at_Data(self, data, node):
        index = self.getdataIndex(data) # 해당 데이터의 인덱스 가져온다.
        if 0 <= index:
            self.Insert_Node_at_Index(index, node) #해당 인덱스 찾아서 거기다 값 삽입
        else:
            return -1
    
    # Delete data at given index
    def Delete_at_Index(self, idx):
        curn_i = 0
        curn = self.head
        prevn = None
        nextn = self.head.next
        if idx == 0:
            self.head = nextn
        else:
            while curn_i < idx:
                if curn.next:
                    prevn = curn
                    curn = nextn
                    nextn = nextn.next
                else:
                    break
                curn_i += 1
            if curn_i == idx:
                prevn.next = nextn
            else:
                return -1
    
    # Empty linked list
    def clear(self):
        self.head = None
    
    # 출력
    def print(self):
        curn = self.head
        string = ""
        while curn:
            string += str(curn.data)
            if curn.next:
                string += "->"
            curn = curn.next
        print(string)