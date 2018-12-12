# Stack Implementation in python

class Node:
    def __init__(self, val):
        self.val = val
        self.next = Node

class Stack:
    def __init__(self):
        self.top = None

    # checks if the stack is empty by check if top is empty
    def isEmpty(self):
        return self.top is None

    # pushes new element into stack
    def push(self,val):
        node = Node(val)
        node.next = self.top
        self.top = node

    # pops an element from the top of the stack
    def pop(self):
        if self.top is None:
            return Exception("Empty Stack Exception")

        item = self.top.val
        self.top = self.top.next

        return item

    # returns the top of the stack
    def peek(self):
        if self.top is None:
            return Exception("Empty Stack Exception")
        else:
            return self.top.val


# main function
if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)

    print("top", stack.peek()) # 40

    stack.pop()

    print("top", stack.peek()) # 30

    stack.pop()

    print("popped", stack.pop()) # 20

    stack.pop()

    print("is empty?", stack.isEmpty()) # true

    print("top", stack.peek()) # exception

