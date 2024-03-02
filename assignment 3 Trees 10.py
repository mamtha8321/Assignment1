class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_odd_level_nodes(root):
    def traverse(node, level):
        if node is None:
            return

        if level % 2 != 0:
            print(node.val)

        traverse(node.left, level+1)
        traverse(node.right, level+1)

    traverse(root, 1)

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print_odd_level_nodes(root)  # Output: 1 4 5 7
