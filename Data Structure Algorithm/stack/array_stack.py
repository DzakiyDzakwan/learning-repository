class ArrStack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def search(self, item):
        try:
            index = self.items.index(item)
            return index
        except ValueError:
            return -1