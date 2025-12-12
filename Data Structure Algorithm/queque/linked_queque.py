class Node() :
    def __init__(self, value) :
        self.value = value
        self.next = None

class LinkedQueQue() :
    def __init__(self) :
        self.front = None
        self.rear = None
        self._size = 0

    def size(self) :
        return self._size
    
    def display(self) :
        elements = []
        current = self.front
        while current:
            elements.append(current.value)
            current = current.next
        return elements
    
    def isEmpty(self) :
        return self._size == 0
    
    def enqueue(self, item) :
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self) :
        if self.isEmpty():
            raise IndexError("Dequeue from empty queue")
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        self._size -= 1

    def front(self) :
        if self.isEmpty():
            raise IndexError("Peek from empty queue")
        return self.front.value
    
    def rear(self) :
        if self.isEmpty():
            raise IndexError("Peek from empty queue")
        return self.rear.value
    
    def clear(self) :
        self.front = None
        self.rear = None
        self._size = 0