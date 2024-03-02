class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_height(root):
    """
    Returns the height of a perfect binary tree rooted at the given node
    """
    height = 0
    while root.left is not None:
        height += 1
        root = root.left
    return height

def node_sum(root):
    if root is None:
        return 0

    # Calculate the total number of nodes in the perfect binary tree
    height = get_height(root)
    total_nodes = 2**(height+1) - 1

    # Traverse the tree and add up the values of each node
    stack = [root]
    node_sum = 0
    while stack:
        node = stack.pop()
        node_sum += node.val
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)

    return node_sum

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(node_sum(root))  # Output: 28
