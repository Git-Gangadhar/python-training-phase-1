class Node:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_node(node, data):
    if node is None:
        return Node(data)
    if data < node.data:
        node.left = insert_node(node.left, data)
    else:
        node.right = insert_node(node.right, data)
    return node

def sum_left_right(node):
    if node is None:
        return 0
    return node.data + sum_left_right(node.left) + sum_left_right(node.right)

# Create a binary search tree
root = None
root = insert_node(root, 5)
root = insert_node(root, 3)
root = insert_node(root, 7)
root = insert_node(root, 2)
root = insert_node(root, 4)
root = insert_node(root, 6)
root = insert_node(root, 8)

# Calculate the sum of left and right subtrees
sum_left = sum_left_right(root.left)
sum_right = sum_left_right(root.right)

# Print the results
print("Sum of left subtree:", sum_left)
print("Sum of right subtree:", sum_right)