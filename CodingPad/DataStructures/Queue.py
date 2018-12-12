# Queue implementation in python

# queue node
class Node:
    def __init__(self, val):
        self.val =  val
        self.next = None

# queue class with its functions
class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    # adds node to the back of the queue
    def enqueue(self, val):
        node = Node(val)

        if self.front is None:
            self.front = node
            self.back = self.front

        else:
            self.back.next = node
            self.back = node

    # removes node from the front of the queue
    def dequeue(self):
        if self.front is None:
            return Exception("Empty queue exception")

        item = self.front.val
        self.front = self.front.next

        return item

    # returns the first item of the queue if not empty
    def peek(self):
        if self.front is None:
            return Exception("Empty queue exception")

        return self.front.val

# main function
# create queue and use functions
if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    print(queue.peek()) # 10
    queue.dequeue() # remove 10
    print(queue.peek()) # 20
    queue.enqueue(50) # at 50 to the back
    print(queue.peek()) # 20
    queue.dequeue() # remove 20
    print(queue.peek()) # 30
    queue.dequeue() # remove 30
    print(queue.peek()) # 40
    queue.dequeue() # remove 40
    print(queue.peek()) # 50
    print(queue.dequeue()) # remove 50
    print(queue.dequeue()) # Empty queue exception

