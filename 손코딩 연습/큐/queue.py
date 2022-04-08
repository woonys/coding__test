from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque() # deque로 구현
    
    #Add an element
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.popleft() # O(1)
    
    def display(self):
        print(self.queue)
    
    def size(self):
        return len(self.queue)
    