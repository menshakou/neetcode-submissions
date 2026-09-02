class Node:

    def __init__(self, value=None):
        self.val = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)

        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        
    def append(self, value: int) -> None:
        new_node = Node(value)

        wall = self.tail
        last_node = self.tail.prev

        new_node.next = wall
        new_node.prev = last_node
        
        wall.prev = new_node  
        last_node.next = new_node


    def appendleft(self, value: int) -> None:
        new_node = Node(value)

        head = self.head
        next_node = self.head.next

        new_node.prev = head
        new_node.next = next_node
        
        self.head.next = new_node
        next_node.prev = new_node

    def pop(self) -> int:
        if not self.isEmpty():
            result = self.tail.prev
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail

            return result.val
        else:
            return -1

        
    def popleft(self) -> int:
        if not self.isEmpty():
            result = self.head.next
            self.head.next = self.head.next.next
            self.head.next.prev = self.head

            return result.val
        else:
            return -1
        
