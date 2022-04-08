'''스택 자료구조 구현'''

# creating a stack

from curses import is_term_resized


class Stack:
    
    # 리스트로 스택 생성
    def __init__(self):
        self.top = []
        
    def __len__(self):
        return len(self.top)
  
    #check if it's empty
    def is_empty(self):
        return len(self.top) == 0
    
    #push
    def push(self, data):
        self.top.append(data)
    
    #pop
    def pop(self, data):
        if not self.is_empty():
            return self.top.pop(-1)
        else:
            print("This stack is empty.")
            exit()
    
    def peek(self):
        if not self.is_empty():
            return self.top[-1]
        else:
            print("This stack is empty.")
            exit()
    # is_full? -> 파이썬에서 리스트는 동적 배열 -> 알아서 사이즈 늘려주기 때문에 IS_full 필요 X