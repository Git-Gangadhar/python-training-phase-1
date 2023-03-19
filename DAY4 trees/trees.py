class Node:


    def ___init___(self,root,value):
        self.root=value
        self.left=None
        self.right=None
# class bst:
    def add_element(self,root,value):
        new_node=Node(value)
        if new_node.data<root.data:
            if root.left!=None:
                return self.add_element(self.left,value)
            else:
                root.left=new_node
        else:
            if root.right!=None:
                self.add_element(self.right,value)
#             else:
#                 root.right=new_node
# # ob=bst()
ob.add_element(5)
ob.add_element(7)
ob.add_element(8)
#
#
class Node:
    def ___init___(self,root,value):
        self.root=value
        self.left=None
        self.right=None
class BSTree:
    def add_element(self,root,value):
        new_node = Node(value)
        if new_node.data < root.data:
            if root.left != None:
                return self.add_element(self.left, value)
            else:
                root.left = new_node
        else:
            if root.right != None:
                self.add_element(self.right, value)
            else:
                root.right = new_node

    def inorder(self,root):
        if root.left!=None:
            self.inorder(root.left)
        print(root.data)
        if root.right!=None:
         def inorder(self, root):
             if root.left != None:
                 self.inorder(root.left)
        print(root.data)
             if root.right != None:

ob=BSTree()
root=node(7)
ob.add_element(root,5)
ob.add_element(root,4)
ob.inorder(root)