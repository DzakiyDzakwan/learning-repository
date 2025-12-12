from collections import deque

class DequeQueque():
    def __init__(self):
        self.items = deque()

    def size(self):
        return len(self.items)
    
    def display(self):
        return list(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Dequeue from empty queue")
        return self.items.popleft()
    
    def front(self):
        if self.isEmpty():
            raise IndexError("Peek from empty queue")
        return self.items[0]
    
    def rear(self):
        if self.isEmpty():
            raise IndexError("Peek from empty queue")
        return self.items[-1]
    
    def clear(self):
        self.items.clear()