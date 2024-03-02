class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_level_sum(root):
    if root is None:
        return 0

    queue = [root]
    max_sum = root.val
    while queue:
        level_sum = 0
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)
            level_sum += node.val
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        if level_sum > max_sum:
            max_sum = level_sum

    return max_sum

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(max_level_sum(root))  # Output: 15
