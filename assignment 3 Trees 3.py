class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def preorder_traversal(node):
    if node is not None:
        print(node.data, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.data, end=' ')
        inorder_traversal(node.right)

def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end=' ')
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Pre-order traversal:")
preorder_traversal(root)  # output: 1 2 4 5 3

print("\nIn-order traversal:")
inorder_traversal(root)  # output: 4 2 5 1 3

print("\nPost-order traversal:")
postorder_traversal(root)  # output: 4 5 2 3 1
