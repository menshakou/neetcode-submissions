class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        if self.head == None or index < 0:
            return -1

        curr = self.head

        for i in range(index):
            if curr.next == None:
                return -1
            curr = curr.next
        
        return curr.val

    def insertHead(self, val: int) -> None:
        node = Node(val)

        if self.head:
            node.next = self.head

        self.head = node


        if self.tail == None:
            self.tail = node
        

    def insertTail(self, val: int) -> None:
        node = Node(val)

        if self.tail:
            self.tail.next = node
            self.tail = node
        elif self.tail == None:
            self.tail = node
            self.head = node
        

    def remove(self, index: int) -> bool:
        if self.head == None or index < 0:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        curr = self.head

        for i in range(index - 1):
            if curr.next == None:
                return False
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next
            if curr.next == None:
                self.tail = curr

            return True
        else:
            return False
        

    def getValues(self) -> List[int]:
        result = []

        curr = self.head

        while(curr != None):
            result.append(curr.val)
            curr = curr.next
        
        return result
        
