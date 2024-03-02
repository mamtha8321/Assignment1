class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_subtrees_with_sum_x(root, x):
    def count_subtrees(node):
        nonlocal count
        if node is None:
            return 0

        # Calculate the sum of the left and right subtrees
        left_sum = count_subtrees(node.left)
        right_sum = count_subtrees(node.right)

        # Check if the subtree rooted at the current node sums up to x
        if node.val + left_sum + right_sum == x:
            count += 1

        # Return the sum of the current node and its subtrees
        return node.val + left_sum + right_sum

    count = 0
    count_subtrees(root)
    return count

# Example usage
root = TreeNode(5)
root.left = TreeNode(-10)
root.right = TreeNode(3)
root.left.left = TreeNode(9)
root.left.right = TreeNode(8)
root.right.left = TreeNode(-4)
root.right.right = TreeNode(7)

print(count_subtrees_with_sum_x(root, 7))  # Output: 2
