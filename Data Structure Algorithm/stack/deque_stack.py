from collections import deque

class DequeStack:
    def __init__(self):
        self.stack = deque()

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.stack[-1]
    
    def search(self, item):
        try:
            index = list(self.stack).index(item)
            return index
        except ValueError:
            return -1