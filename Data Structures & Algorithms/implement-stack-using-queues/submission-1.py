class Node:

    def __init__(self, value=-1, next=None):
        self.val = value
        self.next = next

class Queue:

    def __init__(self):
        self.dummy = Node()
        self.tail = self.dummy
        self.size = 0

    def push(self, val):
        newNode = Node(val)
        
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def pop(self):
        if self.size == 0:
            return -1

        result = self.dummy.next
        self.dummy.next = self.dummy.next.next
        self.size -= 1

        if self.size == 0:
            self.tail = self.dummy

        return result.val

    def peek(self):
        if self.size == 0:
            return -1
        return self.dummy.next.val

    def empty(self):
        return self.size == 0

class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        

    def push(self, x: int) -> None:
        self.q2.push(x)

        while not self.q1.empty():
            curr = self.q1.pop()
            self.q2.push(curr)

        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp

    def pop(self) -> int:
        return self.q1.pop()
        

    def top(self) -> int:
        return self.q1.peek()
        

    def empty(self) -> bool:
        return self.q1.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()