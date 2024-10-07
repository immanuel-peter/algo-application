class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class IntStack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.top is None:
            raise IndexError("Popping from empty stack")
        value = self.top.value
        self.top = self.top.next
        self.count -= 1
        return value

    def peek(self):
        if self.top is None:
            raise IndexError("Peeking from empty stack")
        return self.top.value

    def size(self):
        return self.count