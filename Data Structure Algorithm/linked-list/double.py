class Node():
    def __init__(self, value, previous = None, next = None):
        self.value = value
        self.previous = previous
        self.next = next

class DoubleLinkedList():
    def __init__(self):
        self.tail = None
        self.head = None

    def getHead(self):
        if self.head:
            return self.head.value
        
        raise Exception("Empty")

    def getTail(self):
        if self.tail:
            return self.tail.value
        
        raise Exception("Empty")

    def insertBegining(self, value):
        if self.head:
            node = Node(value, None, self.head)
            self.head.previous = node
            self.head = node
            return
        else :
            node = Node(value, None, None)
            self.head = node
            self.tail = node
            return

    def insertEnd(self, value):
        if self.tail is None:
            node = Node(value, None, None)
            self.head = node
            self.tail = node
            return
        
        node = Node(value, self.tail, None)
        self.tail.next = node
        self.tail = node
        return

    def deleteBeginning(self):
        if self.head:
            self.head.previous = None
            self.head = self.head.next
            return
        
        raise Exception("list is empty")
    
    def printFoward(self):
        if self.head is None:
            print("list is empty")
            return

        itr = self.head
        values = ""
        
        while itr:
            if itr.previous and itr.next:
                values += f"<== {itr.value} ==>"
            elif itr.next is None:
                values += f"<== {itr.value}(tail)"
            else:
                values += f"{itr.value}(head) ==>"
        
            itr = itr.next

        print(values)

    def printBackward(self):
        if self.tail is None:
            print("list is empty")
            return
        
        itr = self.tail
        values = ""

        while itr:
            if itr.previous and itr.next:
                values += f"<== {itr.value} ==>"
            elif itr.next is None:
                values += f"{itr.value}(tail) ==>"
            else:
                values += f"<== {itr.value}(head)"
        
            itr = itr.previous
        
        print(values)

    def searchValue(self, value):
        if self.head is None:
            print("list is empty")

        if self.head == value or self.tail == value:
            return True

        itr = self.head
        
        while itr:
            if itr.value == value:
                return True
            itr = itr.next

        return False 

    def deleteValue(self, value):
        if self.head is None:
            print("list is empty")
        
        if self.head.value == value:
            self.head = self.head.next
            self.head.previous = None
            return
        
        if self.tail.value == value:
            self.tail = self.tail.previous
            self.tail.next = None
            return

        itr = self.head

        while itr:
            if itr.next.value == value:
                itr.next = itr.next.next
                itr.next.previous = itr
                return
            
            itr = itr.next


double = DoubleLinkedList()
double.insertEnd(3)
double.insertBegining(2)
double.insertBegining(1)
double.insertEnd(4)
double.insertEnd(5)
double.printFoward()
double.deleteValue(3)
double.printFoward()