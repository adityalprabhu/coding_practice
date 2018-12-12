# Implementation of a binary search tree in python

class Node:
    def __init__(self, val, parent=None):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insertNode(self, val, current, node):

        if val < current.val:

            if current.left is None:
                current.left = node
            else:
                self.insertNode(val, current.left, node)
        else:
            if current.right is None:
                current.right = node
            else:
                self.insertNode(val, current.right, node)


    def insert(self, val):
        node = Node(val)

        if self.root is None:
            self.root = node
        else:
            self.insertNode(val, self.root, node)


    def inorder(self, node, traversed=[]):
        if node is not None:
            traversed = self.inorder(node.left, traversed)
            traversed.append(node.val)
            traversed = self.inorder(node.right, traversed)

        return traversed

    def preorder(self, node, traversed=[]):
        if node is not None:
            traversed.append(node.val)
            traversed = self.preorder(node.left, traversed)
            traversed = self.preorder(node.right, traversed)

        return traversed

    def postorder(self, node, traversed=[]):
        if node is not None:
            traversed = self.postorder(node.left, traversed)
            traversed = self.postorder(node.right, traversed)
            traversed.append(node.val)

        return traversed



if __name__ == '__main__':
    tree = Tree()
    print("construction of a tree")

    tree.insert(10)
    tree.insert(5)
    tree.insert(20)
    tree.insert(3)
    tree.insert(7)
    tree.insert(11)
    tree.insert(4)
    tree.insert(15)

    print(tree.preorder(tree.root))
    print(tree.inorder(tree.root))
    print(tree.postorder(tree.root))