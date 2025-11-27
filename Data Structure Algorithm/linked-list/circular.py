class Node() :
    def __init__(self, previous = None, value = None, next = None):
        self.previous = previous
        self.next = next
        self.value = value

class CircularSingleLinkedList():
    def __init__(self):
        self.head = None

    def printList(self):

        if self.head is None:
            print("List is empty")

        values = ""
        itr = self.head

        while itr.next != self.head:
            values += f" {itr.value} =>"
            itr = itr.next

        values += f" {itr.value}"
        
        print(values)

    def insertFirst(self, value):
        if self.head is None:
            self.head = Node(value = value, next = None)
            self.head.next = self.head
            return
        
        itr = self.head
        
        while itr.next != self.head:
            itr = itr.next

        node = Node(value = value, next = self.head)
        itr.next = node
        self.head = node

    def insertLast(self, value):
        if self.head is None:
            node = Node(value = value, next = None)
            self.head = node
            self.head.next = node
            return
        
        itr = self.head
        
        while itr.next != self.head:
            itr = itr.next

        node = Node(value = value, next = self.head)
        itr.next = node

        return

    def deleteFirst(self):
        if self.head is None:
            return
        
        itr = self.head
        while itr.next != self.head:
            itr = itr.next

        self.head = self.head.next
        itr.next = self.head
        return
    
    def deleteLast(self):
        if self.head is None:
            print("list is empty")
            return

        itr = self.head

        while itr.next.next != self.head:
            itr = itr.next

        itr.next = self.head
        return


circular_single = CircularSingleLinkedList()
circular_single.insertFirst(3)
circular_single.insertFirst(2)
circular_single.insertFirst(1)
circular_single.insertLast(4)
circular_single.insertLast(5)
circular_single.deleteFirst()
circular_single.deleteLast()
circular_single.printList()


class CircularDoubleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def printFoward(self):
        if self.head is None:
            print('list is empty')
            return
        
        values = ""
        itr = self.head
        while itr.next != self.head:
            if itr.previous != self.tail:
                values += f"<== {itr.value} ==>"
            else:
                values += f"{itr.value} ==>"
            itr = itr.next
        
        values += f"<== {itr.value}"
        print(values)

    def insertFirst(self, value):
        if self.head is None:
            node = Node(value = value, previous = None, next = None)
            self.tail = node
            self.head = node

            self.head.next = self.head
            self.head.previous = self.head
            return
        
        itr = self.head

        while itr.next != self.head:
            itr = itr.next

        node = Node(value = value, previous = self.tail, next = self.head)
        node.next.previous = node
        itr.next = node
        self.head = node
        return

    def insertLast(self, value):
        if self.head is None:
            node = Node(value=value, previous=None, next=None)
            node.next = node
            node.previous = node

            self.head = node
            self.tail = node
            return
        
        itr = self.head
        while itr.next != self.head:
            itr = itr.next
        
        node = Node(value=value, previous=itr, next=self.head)
        self.tail = node
        self.head.previous = node
        node.previous.next = node
        return

    def deleteFirst(self):
        if self.head is None:
            return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        
        self.head = self.head.next
        self.head.previous = self.tail
        self.tail.next = self.head
        return
    
    def deleteLast(self):
        if self.head is None:
            return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        
        self.tail = self.tail.previous
        self.tail.next = self.head
        self.head.previous = self.tail

circular_double = CircularDoubleLinkedList()
circular_double.insertFirst(3)
circular_double.insertFirst(2)
circular_double.insertFirst(1)
circular_double.insertLast(4)
circular_double.insertLast(5)
circular_double.deleteFirst()
circular_double.deleteLast()
circular_double.printFoward()