class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            queue = [self.root]

            while queue:
                node = queue.pop(0)

                if node.left is None:
                    node.left = new_node
                    break
                else:
                    queue.append(node.left)

                if node.right is None:
                    node.right = new_node
                    break
                else:
                    queue.append(node.right)

    def print_tree(self):
        if self.root is None:
            print("Empty tree")
        else:
            queue = [self.root]

            while queue:
                node = queue.pop(0)

                print(node.data, end=' ')

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)
tree = BinaryTree()

tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)

tree.print_tree()  # output: 1 2 3 4 5 6
