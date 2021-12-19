class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [0] * k
        self.size = k
        self.front_p = 0
        self.rear_p = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull() != True:
            self.rear_p= (self.rear_p + 1) % self.size
            self.queue[self.rear_p] = value
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.front_p <= self.rear_p:
            self.queue[self.front_p] = 0
            self.front_p = (self.front_p +1) % self.size
            return True
        else:
            self.isEmpty()
        
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.front_p]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear_p]
        
    def isEmpty(self) -> bool:
        if self.front_p == self.rear_p:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if (self.rear_p + 1) % self.size == (self.front_p % self.size):
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()