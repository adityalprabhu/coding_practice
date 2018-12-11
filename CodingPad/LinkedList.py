# LinkedList Implementation in python


# Node Class
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# LinkedList Class
class LinkedList:
    def __init__(self):
        self.head = None


# Insert new node at the end
def insertAtEnd(head, node):
    while head.next is not None:
        head = head.next
    head.next = node


# Insert a new node
def insert(ll, val):
    node = Node(val)
    if ll.head is None:
        ll.head = node
    else:
        insertAtEnd(ll.head, node)


# traverse all nodes in linked list
def traverseAll(ll):
    nextNode = ll.head
    while nextNode is not None:
        print(nextNode.val)
        nextNode = nextNode.next


# remove node from linked list
def removeNode(ll, node):
    nnode = ll.head

    # base condition if head of linked list is the node to be removed
    if ll.head.val == node:
        ll.head = ll.head.next

    # traverse linked list and find the node to be removed
    while nnode.next is not None:
        if nnode.next.val == node:
            nnode.next = nnode.next.next
            return "Node removed"
            break

        nnode = nnode.next

    return "Node not found"


# Main function
if __name__ == '__main__':
    ll = LinkedList()
    insert(ll, 10)
    insert(ll, 20)
    insert(ll, 30)
    insert(ll, 40)
    insert(ll, 50)
    insert(ll, 60)
    insert(ll, 70)
    removeNode(ll, 10)
    print(removeNode(ll, 40))
    print(removeNode(ll, 80))
    traverseAll(ll)
