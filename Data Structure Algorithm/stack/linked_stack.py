class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedStack():
    def __init__(self):
        self.top = None
        self._size = 0

    def is_empty(self):
        return self._size == 0
    
    def size(self):
        return self._size
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            return None
        popped_value = self.top.value
        self.top = self.top.next
        self._size -= 1
        return popped_value
    
    def peek(self):
        if self.is_empty():
            return None
        return self.top.value
    
    def search(self, item):
        current = self.top
        index = 0
        while current:
            if current.value == item:
                return index
            current = current.next
            index += 1
        return -1