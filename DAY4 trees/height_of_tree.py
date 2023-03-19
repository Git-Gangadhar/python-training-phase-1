class Node:

    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BSTree:
    def add_element(self, root, value):
        new_node = Node(value)
        if new_node.data < root.data:
            if root.left is not None:
                self.add_element(root.left, value)
            else:
                root.left = new_node
        else:
            if root.right is not None:
                self.add_element(root.right, value)
            else:
                root.right = new_node
    def inorder(self,root):
        if(root is not None):
            self.inorder(root.left)
            print(root.data,end=' ')
            self.inorder(root.right)
    def preorder(self,root):
        if(root is not None):
            self.preorder()
    def height(self, root):
        if root == None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
ob=BSTree()
root=Node(10)
ob.add_element(root, 50)
ob.add_element(root, 40)
ob.add_element(root, 80)
ob.add_element(root, 506)
ob.add_element(root, 50)
ob.inorder(root)
print()
a=ob.height(root)

print(a)

