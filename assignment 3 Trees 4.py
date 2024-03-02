class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def print_leaves(node):
    if node is not None:
        if node.left is None and node.right is None:
            print(node.data)
        else:
            print_leaves(node.left)
            print_leaves(node.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print_leaves(root)  # output: 4 5 6 7
