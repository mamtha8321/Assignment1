class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_of_left_leaves(root):
    if root is None:
        return 0

    # Check if the left child of the root is a leaf node
    if root.left is not None and root.left.left is None and root.left.right is None:
        left_sum = root.left.val
    else:
        left_sum = 0

    # Recursively calculate the sum of left leaves in the left and right subtrees
    return left_sum + sum_of_left_leaves(root.left) + sum_of_left_leaves(root.right)

# Example usage
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(sum_of_left_leaves(root))  # Output: 24
