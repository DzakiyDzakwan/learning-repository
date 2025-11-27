class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return f"node: {self.value}, next : {self.next}"

class SingleLinkedList():
    def __init__(self):
        self.head = None

    def insertFirst(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insertEnd(self, data):
        # if list still empty
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insertList(self, data):
        for datum in data:
            self.insertEnd(datum)

    def printList(self):
        if self.head is None:
            print("List is empty")
                
        itr = self.head
        listr = ""

        while itr:
            if itr.next is None :
                listr += str(itr.value)
            else :
                listr += str(itr.value) + " => "
            itr = itr.next
            
        
        print(listr)

    def searchValue(self, value):
        if self.head is None:
            print("List is empty")
            return
        
        itr = self.head

        while itr:
            if itr.value == value:
                print(f"{value} ditemukan")
                return
            
            itr = itr.next

    def length(self)->int:
        i = 0
        itr = self.head

        while itr:
            i += 1
            itr = itr.next
        
        return i

    def deleteAt(self, index):
        if index < 0 or index >= self.length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0

        while itr.next:
            
            if count == index-1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count += 1

    def insertAt(self, value, index):
        if index<0 or index>=self.length():
            raise Exception("Invalid Index")
        
        if index == 0 :
            self.head = Node(value, self.head.next)
            return
        
        count = 0
        itr = self.head
        
        while itr:
            if count == index - 1:
                itr.next = Node(value, itr.next)
                break

            itr = itr.next
            count += 1

    def insertAfterValue(self, target, value):
        itr = self.head

        while itr:
            if itr.value == target:
                itr.next = Node(value, itr.next.next if itr.next else None)
                return

            itr = itr.next
        
        print("target value not found")

    def deleteValue(self, value):
        if value == self.head.value:
            self.head = self.head.next
            return

        itr = self.head

        while itr.next:
            if itr.next.value == value:
                itr.next = itr.next.next
                return
            
            itr = itr.next
        print("target value not found")
                
single = SingleLinkedList()

single.insertFirst(10)
single.insertFirst(9)
single.insertEnd(11)
single.printList()
single.searchValue(12)
single.insertList([12,13,14,15])
single.printList()
single.deleteAt(6)
single.printList()
single.insertAfterValue(14, 10.5)
single.printList()
single.deleteValue(9)
single.printList()